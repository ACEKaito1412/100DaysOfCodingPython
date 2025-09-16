from flask import Blueprint, render_template, request, session, redirect, url_for
from app.service.api_client import AuthApi, ProductApi, UserApi


auth_client = None

def init_login(api_client_auth:AuthApi):
    global auth_client
    auth_client = api_client_auth

login_bp = Blueprint("login", __name__)

@login_bp.route("/", methods=["POST", "GET"])
def login():

    error = None
    if request.method == "POST":
        data = request.form
        if not data or "email" not in data or "password" not in data:
            error = "Invalid input"

        try:
            email = data["email"]
            password = data["password"]


            response_data = auth_client.login(email, password)

            session["token"] = response_data["token"]

            return redirect(url_for("dashboard.home"))
        except Exception as e:
            return redirect(url_for("login.login"))
            
    
    return render_template("login.html", error=error)

@login_bp.route("/logout")
def log_out():
    session.clear()
    return redirect(url_for("login.login"))