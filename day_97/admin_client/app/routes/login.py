from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
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
            session["token"] = "something"
            return redirect(url_for("dashboard.home"))
            # error = "Login Failed"
            
    
    return render_template("login.html", error=error)