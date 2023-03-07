from flask import Flask, request, render_template, url_for
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

posts = [
    {
        'author': 'Nicole Agutu',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Kunta Handel',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 23, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/search", methods=['POST', 'GET'])
def search():
    return render_template('search.html', title='Search')


@app.route('/bot', methods=['POST'])
def bot():
    user_msg = request.values.get('Body', '').lower()
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    
    return str(bot_resp)



if __name__ == '__main__':
    app.run(debug=True)