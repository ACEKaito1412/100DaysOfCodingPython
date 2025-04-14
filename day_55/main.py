from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route('/guess/<name>/<int:age>')
def guest(name, age):
    return f"Hi {name}, you are {age} years old."


if __name__ == "__main__":
    app.run(debug=True)