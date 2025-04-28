# Cheerify

Welcome to the **Cheerify** repository! This project is designed to evaluate any feedback, review, comments users in any E-commerce website, social media. It check any review from a users and check its polarity as positive or negative. If the review is positive the review is stored effortlessly
but if negative which is checked through **Sentiment analysis** and then a neutral alternative is suggested to users using **Sentiment transfer**, If user likes it, user can post it if user don't like the alternative the original review is posted.

The purpose of this project is to maintain the integrity and ethics at internet by taking measures and check rather than forcing users to do the company desire to prevent there reputation.

## Key Features
- Prevent Negative review
- Suggest Neutral alternative
- Do not enforce direction to user
- Considerate to user's opinions
- Preventive measure for platform
- Easy integration to various platforms

## Technologies Used
- Sentiment analysis
- Sentiment Transfer
- Full stack
    - Python - Flask
    - HTML
    - JavaScript
    - CSS
    - PostgreSql

## Setup
1. Download the repository
2. Open folder in VS code
3. Open terminal and create a virtual environment using
    - Windows:
      ``` bash
       python -m venv .venv
      ```
    - Mac and linux :
      ```bash
      python3 -m venv .venv
      ```

4. for windows OS only :- open system powershell in base directory and enter 
``` bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
5. Now to activate virtual environment open cmd in the project folder directory in vs code or the cmd
    - windows :-
      ``` bash
      .venv\Scripts\activate.bat
      ```
    - Mac Os :-
      ``` bash
      source .venv/bin/activate
      ```
    - linux :-
      ``` bash
      source .venv/bin/activate
      ```

6. Your virtual environment is activated if cmd shows (.venv) before the directory Eg: (.venv) D:\minor2>
7. Now install all the dependencies by writing command: 
    - windows:
      ``` bash
      pip install requirements.txt
      ```
    - Mac and linux:
      ``` bash
      pip3 install requirements.txt
      ```
    # requirements.txt file in provided in the repo with contains all the dependencies with the supported versions

setup completed

## Model training

1. Open Neutral folder
2. Run neutral.py file while inside the virtual environment
3. Model training is the essential part of a AI project as the all the model learning can't be shared through GIT due to large size
4. The model learning may take around 10-20 minutes based on the system specifications and the size of learnings can extends upto 20GB.

## Database setup
1. In project directory open cmd in vsCode and type:
windows: 
``` bash
python
```
 Mac or linux:
 ``` bash
python3
```
2. Then type:
``` bash
from app import db, app
``` 
3. Then type:
``` bash
with app.app_context():
    db.create_all()
```
4. A Sqlite database is created
5. You can change database of your choice by changing the Databse URL in app.py line. 11
6. The procedure is same for every database 


## Run project

Type in cmd :
windows:
```bash
python app.py
```
Mac and linux:
``` bash
python3 app.py
```

## NOTE: Go through all the files and check or alter all the paths in all the files as per your system
