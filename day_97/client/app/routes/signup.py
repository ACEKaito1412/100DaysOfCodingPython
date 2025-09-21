from flask import Blueprint, render_template, request, session, redirect, url_for
from app.service.api_client import UserApi


user_client = None

def init_signup(api_client_user:UserApi):
    global user_client
    user_client = api_client_user

signup_bp = Blueprint("signup", __name__)

@signup_bp.route("/", methods=["POST", "GET"])
def home():

    error = None
    if request.method == "POST":
        data = request.form
        if not data or "email" not in data or "password" not in data or "name" not in data:
            error = "Invalid input"

        try:
            response_data = user_client.create(data.to_dict())

            return redirect(url_for("shop.home"))
        except Exception as e:
            return redirect(url_for("login.login"))
            
    
    return render_template("signup.html", error=error)
