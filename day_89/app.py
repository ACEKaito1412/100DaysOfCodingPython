from flask import Flask, render_template, request, redirect
from db_setup import db, User, Todo, add_new_user, get_user_by_email, add_new_todo, update_todo, get_user_todos
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


sample_todos = [
    Todo(id = 0, user_id = 0, task = "Feed Dogs", deadline_date = "01-02-2025" , status = False),
    Todo(id = 1, user_id = 0, task = "Relax for 30 Mins", deadline_date = "01-02-2025" , status = True)
]


app  = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"

db.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route('/', methods=['POST', 'GET'])
def home():
    todos = sample_todos
    name = ""
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect('/login')

        todo = Todo(
            user_id = current_user.id,
            task = request.form['task'],
            status = False,
            deadline_date = datetime.strptime(request.form['deadline'], "%Y-%m-%d")
        )

        add_new_todo(todo)
    
    if current_user.is_authenticated:
        todos = get_user_todos(current_user.id)
        name = current_user.name


    return render_template('index.html', logged_in = current_user.is_authenticated, user_name = name, todos = todos)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        try:
            user = get_user_by_email(email)
            if check_password_hash(user.password, request.form['password']):
                return redirect('/')
            else:
                return redirect('/login')
        except AttributeError:
            return redirect('/login')
        
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        user = User(
            name = request.form['name'],
            email = request.form['email'],
            password = generate_password_hash(request.form['password'], method="pbkdf2", salt_length=8),
        )

        add_new_user(user)

        login_user(user)

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)