from flask import Blueprint, render_template, session
from app.service.api_client import UserApi
from app.util import login_required

user_api = None

user_bp = Blueprint("user", __name__)

def init_user(api_client:UserApi):
    global user_api
    user_api = api_client

@user_bp.route("/", methods=["POST", "GET"])
@login_required
def home():
    user_api.set_token(session["token"])

    data = user_api.get_all()

    return render_template("users.html", data=data)