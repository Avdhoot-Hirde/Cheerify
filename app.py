# --- Imports ---

from flask import Flask, render_template , request ,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# --- App setup ---

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///review.db'  #Can change the URL for any other database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

# --- Sentiment analysis model Initialization ---

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english" ,framework="pt")

# --- Sentiment Transfer Model Initialization ---

model_path = "Neutral/gpt2-sentiment-transfer"
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    model.resize_token_embeddings(len(tokenizer))

# --- Model definition ---

class Neutral(db.Model):
    n_id=db.Column(db.Integer,primary_key=True)
    n_review=db.Column(db.Text,nullable=False)

class Review(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    review=db.Column(db.Text, nullable=True)
    date=db.Column(db.DateTime,default=datetime.now())

    def __repr__(self):
        return '<Task %r>' % self.id

# --- Helper function for analysis ---

def sentiment(rev):
    
    result = classifier(rev)
    return result[0]['label']

# --- Helper function for transfer ---

def neutral(rev):
    
    input_text = rev
    inputs = tokenizer(
        input_text,
        return_tensors='pt',
        padding=True,
        truncation=True
    )

    output_ids = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        pad_token_id=tokenizer.pad_token_id,
        max_length=100,
        num_return_sequences=1,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )
    
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    output=output_text.split('.')
    max=1
    for i in range(2,len(output)):
        if(len(output[max])<len(output[i])):
            max=i
    return output[max]

# --- Routes ---
@app.route('/')
def home():
    tasks=Review.query.order_by(Review.date).all()
    return render_template('index.html',tasks=tasks)


@app.route('/review' , methods=['POST'])
def review_pro():
    data = request.get_json()
    text = data.get('text')
    stage = data.get('stage')
    confirm = data.get('confirm')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    if stage == 'initial':
        senti = sentiment(text)
        if senti == 'NEGATIVE':
            transformed = neutral(text)
            new_neutral=Neutral(n_review=transformed)
            db.session.add(new_neutral)
            db.session.commit()
            return jsonify({
                'sentiment': senti,
                'transformed': transformed,
                'ask_confirmation': True
            })
        else:
            new_review = Review(review=text)
            db.session.add(new_review)
            db.session.commit()
            return jsonify({'sentiment': senti, 'review': text, 'done': True})

    elif stage == 'confirmation':
        if confirm:
            transformed = Neutral.query.all()[0]
            Neutral.query.delete()
            db.session.commit() 
            final_review = str(transformed.n_review)
        else:
            final_review = text

        new_review = Review(review=final_review)
        db.session.add(new_review)
        db.session.commit()
        return jsonify({'review': final_review, 'done': True})

    return jsonify({'error': 'Invalid request'}), 400

# --- Main Body ---
if __name__ == '__main__':
    app.run(debug=True)

