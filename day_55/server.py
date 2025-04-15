from flask import Flask
import random

lucky_n = 0

app = Flask(__name__)

@app.route("/")
def home():
    global lucky_n
    lucky_n = random.randint(1, 10)
    return "<h1>Guess the number</h1>"


@app.route("/<int:n>")
def guess(n):
    if n > lucky_n:
        return "<h2 style='color: blue'>Too high</h2>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='200'>"

    if n < lucky_n:
        return "<h2 style='color: blue'>Too Low</h2>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='200'>"

    if n == lucky_n:
        return "<h2 style='color: blue'>You're so lucky</h2>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='200'>"


if __name__ == "__main__":
    app.run(debug=True)
