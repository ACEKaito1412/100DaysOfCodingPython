from flask import Blueprint, render_template, url_for, redirect, session, request
from app.service.api_client import UserApi, CartApi
from app.util import is_login, login_required

user_client = None
cart_client = None

profile_bp = Blueprint('profile' , __name__)

def init_profile(user_api:UserApi, cart_api:CartApi):
    global user_client, cart_client
    user_client = user_api
    cart_client = cart_api

@profile_bp.route('/', methods=["GET"])
@login_required
def home():
    user_client.set_token(session['token'])
    cart_client.set_token(session['token'])

    user = user_client.get_by_token()
    cart = cart_client.get_by_id('paid')
    return render_template('profile.html', user = user, orders = cart, is_login = is_login())   

@profile_bp.route('/<int:user_id>', methods=["GET", "POST"])
@login_required
def update_profile(user_id):
    print(user_id)
    data = request.form.to_dict()
    

    user_client.set_token(session['token'])

    user = user_client.update(data, user_id)

    return redirect(url_for('profile.home'))