from flask import Flask
from flask import render_template
from blog import Blog
import requests

url = 'https://api.npoint.io/674f5423f73deab1e9a7'


res = requests.get(url=url)
res.raise_for_status()

data = res.json()
post_list = []
for post in data:
    post_list.append(Blog(post["id"], post["body"], post["title"], post["subtitle"], post['image_url']))

print(len(post_list))




app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', blog = post_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    post = post_list[id]

    if post:
        return render_template('post.html', post = post_list[id])
    else:
        return app.redirect('/')

if __name__ == "__main__":
    app.run(debug=True)