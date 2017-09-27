"""Cloud Foundry test"""
from flask import Flask
import os
import pyrebase
config = {
  "apiKey": "AIzaSyCSEsN8V7vjKrEBB0sjgoZs8aG-TLd-suI",
  "authDomain": "forexbygrit.firebaseapp.com",
  "databaseURL": "https://forexbygrit.firebaseio.com",
  "storageBucket": "forexbygrit.appspot.com"
}
firebase = pyrebase.initialize_app(config)
import requests 
r = requests.get('https://forex.1forge.com/1.0.2/quotes?pairs=EURUSD%2CGBPJPY%2CAUDUSD&api_key=o7t3pexnQ7NygogAKovIYhQ362UcmwGM')
app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)

@app.route('/add')
def add():
    db = firebase.database()
    db.child().push(r.json())
    return "add finish"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)