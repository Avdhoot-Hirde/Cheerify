from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import Trainer, TrainingArguments, DataCollatorForLanguageModeling

model_name = "gpt2"

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Set pad token

model = GPT2LMHeadModel.from_pretrained(model_name)
from datasets import Dataset

examples = {
    "text": [
    "Transfer to neutral: The website is confusing. <|endoftext|> The website could be more user-friendly.",
    "Transfer to neutral: The package arrived broken. <|endoftext|> The package had some damage during shipping.",
    "Transfer to neutral: This app is terrible. <|endoftext|> This app has some areas that could be improved.",
    "Transfer to neutral: I didn't enjoy the show. <|endoftext|> The show wasn't my favorite.",
    "Transfer to neutral: I'm not happy with this product. <|endoftext|> I have mixed feelings about this product.",
    "Transfer to neutral: The design is ugly. <|endoftext|> The design is not to my taste.",
    "Transfer to neutral: I hate this movie. <|endoftext|> This movie didn't appeal to me.",
    "Transfer to neutral: The instructions are unclear. <|endoftext|> The instructions could use some clarification.",
    "Transfer to neutral: The service was awful. <|endoftext|> The service could be better.",
    "Transfer to neutral: Shipping was delayed. <|endoftext|> Shipping took longer than expected.",
    "Transfer to neutral: I regret this purchase. <|endoftext|> I’m unsure about this purchase.",
    "Transfer to neutral: Customer support was unhelpful. <|endoftext|> Customer support could have been more helpful.",
    "Transfer to neutral: The product doesn't work. <|endoftext|> The product is not functioning as expected.",
    "Transfer to neutral: The experience was frustrating. <|endoftext|> The experience was less than ideal.",
    "Transfer to neutral: I feel disappointed in this product. <|endoftext|> I have mixed feelings about this product.",
    "Transfer to neutral: This food is disgusting. <|endoftext|> This food could use some improvements.",
    "Transfer to neutral: The quality is poor. <|endoftext|> The quality could be better.",
    "Transfer to neutral: The app is unresponsive. <|endoftext|> The app has performance issues.",
    "Transfer to neutral: This was a waste of time. <|endoftext|> I didn’t find this as useful as I expected.",
    "Transfer to neutral: I feel unsatisfied with my purchase. <|endoftext|> I'm not entirely sure about my purchase.",
    "Transfer to neutral: The website is slow. <|endoftext|> The website could use some performance improvements.",
    "Transfer to neutral: The product didn’t meet my expectations. <|endoftext|> The product was different from what I expected.",
    "Transfer to neutral: This movie was boring. <|endoftext|> The movie didn’t keep my interest.",
    "Transfer to neutral: This restaurant is terrible. <|endoftext|> This restaurant didn’t meet my expectations.",
    "Transfer to neutral: The design is bad. <|endoftext|> The design is not ideal for me.",
    "Transfer to neutral: I hate the color scheme. <|endoftext|> The color scheme is not to my liking.",
    "Transfer to neutral: The customer service was rude. <|endoftext|> The customer service wasn’t very polite.",
    "Transfer to neutral: The product broke after one use. <|endoftext|> The product didn’t last as long as expected.",
    "Transfer to neutral: I can’t recommend this product. <|endoftext|> I’m not sure if this product suits everyone.",
    "Transfer to neutral: The food was awful. <|endoftext|> The food didn’t taste good.",
    "Transfer to neutral: The app crashed. <|endoftext|> The app experienced some crashes.",
    "Transfer to neutral: I feel cheated by this service. <|endoftext|> I’m uncertain about the value of this service.",
    "Transfer to neutral: The sound quality is bad. <|endoftext|> The sound quality could use some improvements.",
    "Transfer to neutral: The staff was unprofessional. <|endoftext|> The staff could have been more professional.",
    "Transfer to neutral: I don't like this place. <|endoftext|> I feel neutral about this place.",
    "Transfer to neutral: The instructions are difficult to follow. <|endoftext|> The instructions could be more straightforward.",
    "Transfer to neutral: The game is unplayable. <|endoftext|> The game has several issues that need fixing.",
    "Transfer to neutral: The app is not intuitive. <|endoftext|> The app could have a more user-friendly interface.",
    "Transfer to neutral: The service was slow. <|endoftext|> The service could be faster.",
    "Transfer to neutral: The food was cold. <|endoftext|> The food was served at a lower temperature than expected.",
    "Transfer to neutral: The room was dirty. <|endoftext|> The room could have been cleaned better.",
    "Transfer to neutral: The design is awful. <|endoftext|> The design is not appealing to me.",
    "Transfer to neutral: I didn’t like the music. <|endoftext|> The music didn’t suit my taste.",
    "Transfer to neutral: This phone is awful. <|endoftext|> This phone has several issues that need fixing.",
    "Transfer to neutral: I am unhappy with the purchase. <|endoftext|> The purchase didn’t meet my expectations.",
    "Transfer to neutral: The app is broken. <|endoftext|> The app has some bugs that need fixing.",
    "Transfer to neutral: The quality is terrible. <|endoftext|> The quality could be much better.",
    "Transfer to neutral: I didn’t like the presentation. <|endoftext|> The presentation could have been improved.",
    "Transfer to neutral: The website is frustrating to use. <|endoftext|> The website could be more user-friendly.",
    "Transfer to neutral: I don’t trust this brand. <|endoftext|> I have some reservations about this brand.",
    "Transfer to neutral: The customer service is slow. <|endoftext|> The customer service could be faster.",
    "Transfer to neutral: The app is confusing. <|endoftext|> The app could use a clearer design.",
    "Transfer to neutral: The food was tasteless. <|endoftext|> The food lacked flavor.",
    "Transfer to neutral: The delivery was late. <|endoftext|> The delivery took longer than expected.",
    "Transfer to neutral: The user interface is bad. <|endoftext|> The user interface could be more intuitive.",
    "Transfer to neutral: The room was uncomfortable. <|endoftext|> The room could have been more comfortable.",
    "Transfer to neutral: This movie was terrible. <|endoftext|> The movie didn’t meet my expectations.",
    "Transfer to neutral: The product isn’t useful. <|endoftext|> The product could be more useful in some situations.",
    "Transfer to neutral: I hate the new update. <|endoftext|> I’m not fond of the new update.",
    "Transfer to neutral: The event was a disaster. <|endoftext|> The event didn’t go as planned.",
    "Transfer to neutral: The furniture is uncomfortable. <|endoftext|> The furniture could be more comfortable.",
    "Transfer to neutral: I am dissatisfied with the experience. <|endoftext|> I’m not fully satisfied with the experience.",
    "Transfer to neutral: The app is full of bugs. <|endoftext|> The app has some bugs that need fixing.",
    "Transfer to neutral: I don't like the new feature. <|endoftext|> The new feature could be better.",
    "Transfer to neutral: The interface is hard to use. <|endoftext|> The interface could be simplified.",
    "Transfer to neutral: The quality of the product is poor. <|endoftext|> The product quality could be improved."
]

}


dataset = Dataset.from_dict(examples)

def tokenize(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=64)

tokenized_dataset = dataset.map(tokenize)



data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False  # No masked LM for GPT
)

training_args = TrainingArguments(
    output_dir="Neutral/gpt2-sentiment-transfer",
    per_device_train_batch_size=2,
    num_train_epochs=5,
    logging_steps=10,
    save_steps=50,
    fp16=False,
    overwrite_output_dir=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator
)

trainer.train()

trainer.save_model("Neutral/gpt2-sentiment-transfer")
tokenizer.save_pretrained("Neutral/gpt2-sentiment-transfer")