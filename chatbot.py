from flask import Flask, request, render_template, url_for
import requests

from functionalities import *


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

'''
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

def predict_class(sentence):
    #filter out predictions below a threshold
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort in descending order of probability
    results.sort(key = lambda x: x[1], reverse = True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list'''

if __name__ == '__main__':
    app.run(debug=True)