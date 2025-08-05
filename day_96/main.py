import os, requests
from dotenv import load_dotenv
from flask import Flask, render_template



app = Flask(__name__)

load_dotenv()

CAT_KEY = os.getenv("CAT_KEY")
LINK = 'https://api.thecatapi.com/v1/images/search'

params = {
    'limit' : 12,
    'format' : 'json'
}

headers = {
    'Content-Type' : 'application/json',
    'x-api-key' : CAT_KEY
}

response = requests.get(url=LINK, params=params, headers=headers)

data = response.json()


@app.route('/')
def home():
    return render_template('index.html', list_items = data)

@app.route('/', method=['POST'])
def vote():
    return

if __name__ == '__main__':
    app.run(debug=True)