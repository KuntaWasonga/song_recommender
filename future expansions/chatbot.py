from flask import Flask, request, render_template, jsonify
import requests

from functionalities import *


app = Flask(__name__)

@app.get("/")
@app.get("/home")
def home():
    return render_template('home.html')


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)