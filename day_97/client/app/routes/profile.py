from flask import Blueprint, render_template, url_for, redirect, session, request
from app.service.api_client import UserApi
from app.util import is_login, login_required

user_client = None

profile_bp = Blueprint('profile' , __name__)

def init_profile(user_api:UserApi):
    global user_client
    user_client = user_api

@profile_bp.route('/', methods=["GET"])
@login_required
def home():
    user_client.set_token(session['token'])

    user = user_client.get_by_token()

    print(user)
    return render_template('profile.html', data = user)

@profile_bp.route('/', methods=['POST'])
@login_required
def update_profile(user_id):
    data = request.form()

    user_client.set_token(session['token'])
    user = user_client.update(data.to_dict(),user_id)
    return redirect(url_for('profle.home'))