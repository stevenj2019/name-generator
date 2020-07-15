from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import requests

app = Flask(__name__)
db = SQLAlchemy(app)

class usernames(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10))

@app.route('/', methods=['GET'])
def api():
    nums = requests.get('')
    alph = requests.get('')
    db.session.add(usernames(zip(name=zip(nums, alph))))
    db.session.commit()
    
