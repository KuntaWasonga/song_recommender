import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

from flask import Flask, request, render_template, url_for
import requests

from functionalities import *

# chat initialization
model = load_model("chatbotmodel.h5")
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/search", methods=['POST', 'GET'])
def search():
    return render_template('search.html', title='Search')


@app.route('/bot', methods=['POST'])
def chatbot_response():
    msg = request.form["msg"]
    #checks is a user has given a name, in order to give a personalized feedback
    if msg.startswith('my name is'):
        name = msg[11:]
        ints = predict_class(msg, model)
        res1 = getResponse(ints, intents)
        res =res1.replace("{n}",name)
    elif msg.startswith('hi my name is'):
        name = msg[14:]
        ints = predict_class(msg, model)
        res1 = getResponse(ints, intents)
        res =res1.replace("{n}",name)
    #if no name is passed execute normally
    else:
        ints = predict_class(msg, model)
        res = getResponse(ints, intents)
    return res

if __name__ == '__main__':
    app.run(debug=True)