from flask import Blueprint, render_template, session, request, flash
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

    if request.method == "POST":
        form_data = request.form

        if not form_data or "name" not in form_data:
            flash("Name data not found")
        elif "id" not in form_data:   
            result = user_api.create(form_data.to_dict())
        else:
            result = user_api.update(user_id=form_data["id"], data=form_data.to_dict())

    data = user_api.get_all()
    return render_template("users.html", data=data)