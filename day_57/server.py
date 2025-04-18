from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests

current_year = datetime.now().year
app = Flask(__name__)



@app.route('/')
def home():
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    res.raise_for_status()

    data = res.json()

    return render_template('blog.html',blog=data)

@app.route('/guess/<name>')
def guess(name : str):
    url_agify = f"https://api.agify.io?name={name}"
    res = requests.get(url=url_agify)
    data_agify = res.json()

    url_genderize = f"https://api.genderize.io?name={name}"
    res = requests.get(url=url_genderize)
    data_genderize = res.json()

    return render_template('guess.html', name=name.capitalize(), age=data_agify['age'], gender=data_genderize['gender'])


@app.route('/get_blog/<int:num>')
def get_blog(num):
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    res.raise_for_status()

    data = res.json()

    return render_template('blog_item.html',blog=data, number=num)


if __name__ == "__main__":
    app.run(debug=True)