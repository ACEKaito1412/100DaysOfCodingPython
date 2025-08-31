from flask import Blueprint, request, jsonify, current_app
from app import db
from app.models.users import Users
from werkzeug.security import check_password_hash
import jwt, datetime


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["POST"])
def login():
    data = request.get_json()

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error" : "Invalid input"}), 400

    user = Users.query.filter_by(email=data["email"]).first()

    if not check_password_hash(user.password, data['password']):
        return jsonify({"error" : "Invalid credentials"}), 401
    
    token = jwt.encode(
        {
            "user_id"   : user.id,
            "role"      : user.role.value,
            "exp"       : datetime.datetime.now() + datetime.timedelta(hours=1)
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({"token" : token}), 200
    
