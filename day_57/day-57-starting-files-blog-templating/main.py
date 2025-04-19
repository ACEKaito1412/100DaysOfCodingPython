from flask import Flask, render_template
from post import Post
import requests

res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
res.raise_for_status()

data = res.json()
post_objects = []
for post in data:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs = post_objects)


@app.route('/post/<int:id>')
def post(id):
    cur_post = [item for item in post_objects if item.id==id]

    return render_template('post.html', blog = cur_post[0])

if __name__ == "__main__":
    app.run(debug=True)
