from flask import Flask, render_template, request
from form import MyForm
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "ahalhsaj-asacas"

bootstrap = Bootstrap5(app)

def check_login(email:str, password:str) -> bool :
    if password == "12345678" and email == 'admin@gmail.com':
        return True

    return False 
    


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if check_login(form.email.data, form.password.data):
            return app.redirect('/success')
        else:
            return app.redirect('/denied')
        return app.redirect('/')
    else:
        return render_template(
            "login.html",
            form = form
        )


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
