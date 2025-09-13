from flask import Blueprint, request, jsonify
from app.models.users import Users
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

users_bp = Blueprint('users', __name__)

# GET all user
@users_bp.route('/', methods=['GET'])
def get_users():
    results = Users.query.all()

    return jsonify([
        {
            "id" : user.id,
            "name" : user.name,
            "email" : user.email,
            "role" : user.role.value
        }
        for user in results
    ]), 200


# GET by ID
@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    result = Users.query.get_or_404(user_id)

    return jsonify({
        "id" : result.id,
        "name" : result.name,
        "email" : result.email,
        "role" : result.role.value
    }), 200


# Create new User
@users_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "password" not in data or "email" not in data:
        return jsonify({"error" : "Invalid data"}), 400
    

    email = data["email"]

    user_exist = Users.query.filter_by(email=email).first()

    if user_exist:
        return jsonify({"error" : "Email already exist"}), 400
    
    new_user = Users(
        name = data["name"],
        email = data["email"],
        password = generate_password_hash(data["password"], "scrypt", 16)
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message" : "User added"}), 200

# UPDATE USER
@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(current_user, user_id):
    user = Users.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({"error": "User not found"}), 400
    try:
        data = request.get_json()

        if "name" not in data or user.name == data["name"]:
            return jsonify({"error" : "No changes found" }), 400
        else:
            user.name = data["name"]
            user.role = data["role"]
            db.session.commit()

    except Exception as e:
        return jsonify({"error" :f"{e}"}), 400
    
    return jsonify({
        "message" : "User updated",
        "user" : {
        "name" : user.name,
        "email" : user.email,
        "role" : user.role
        }
    }), 200