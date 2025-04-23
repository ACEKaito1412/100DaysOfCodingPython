from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']


    return f"<h1>{username} {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)