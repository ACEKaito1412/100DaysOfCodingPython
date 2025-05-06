from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''
ckeditor = CKEditor()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor.init_app(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class CreateNewPost(FlaskForm):
    title = StringField("Blog Title", validators=[DataRequired()])
    subtitle = StringField("Blog Subtitle", validators=[DataRequired()])
    date = StringField("Date", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Image Url", validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField("Add new Post") 



# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for  column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    res  = db.session.execute(db.select(BlogPost)).scalars().all()

    posts = [item.to_dict() for item in res]
    print(len(posts))
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    
    try:
        res = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar_one_or_none()
        print(res)
    except AttributeError:
        return redirect('/')
    else:
        requested_post = res.to_dict()
        return render_template("post.html", post=requested_post)


@app.route("/new_post", methods = ['POST', "GET"])
def add_new_post():
    form = CreateNewPost()

    if form.validate():
        new_blog = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = form.date.data,
            img_url = form.img_url.data,
            author = form.author.data,
            body = form.body.data
        )

        db.session.add(new_blog)
        db.session.commit()

        return redirect("/new_post")
    
    print(form.errors)

    return render_template("make-post.html", form = form, is_edit = True)


@app.route("/edit_post/<int:id>", methods=["POST", "GET"])
def edit_post(id):

    res = db.session.execute(db.select(BlogPost).where(BlogPost.id == id)).scalar()
    form = CreateNewPost(
        title = res.title,
        subtitle = res.subtitle,
        author = res.author,
        date = res.date,
        img_url = res.img_url,
        body = res.body
    )

    if form.submit():
        res = db.session.get(BlogPost, id)
        res.title = form.title.data
        res.subtitle = form.subtitle.data
        res.author = form.author.data
        res.img_url = form.img_url.data
        res.body = form.body.data
        db.session.commit()

    return render_template("make-post.html", form=form, is_edit = False, post_id = id)

@app.route("/delete/<int:id>")
def remove_post(id):
    try:
        res = db.session.get(BlogPost, id)
    except ArithmeticError:
        return redirect('/')
    else:
        db.session.delete(res)
        db.session.commit()
        return redirect('/')


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
