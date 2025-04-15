from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        my_html = function()
        return f"<b>{my_html}</b>"
    
    return wrapper


def make_italic(function):
    def wrapper():
        my_html = function()
        return f"<em>{my_html}</em>"
    
    return wrapper


def make_underline(function):
    def wrapper():
        my_html = function()
        return f"<u>{my_html}</u>"
    
    return wrapper

@app.route("/bye")
@make_italic
@make_bold
@make_underline
def bye():
    return "bye"

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello World</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://th.bing.com/th/id/OIP._3K1lj23YM2_UCBfsaHZ6AHaFE?rs=1&pid=ImgDetMain' width='200'>"

@app.route('/guess/<name>/<int:age>')
def guest(name, age):
    return f"Hi {name}, you are {age} years old."


if __name__ == "__main__":
    app.run(debug=True)