from flask import Blueprint, request, jsonify
from app.models.users import Users
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils import token_required
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
@users_bp.route("/get_by_session/", methods=["GET"])
@token_required
def get_user_by_token(current_user):
    result = Users.query.get_or_404(current_user.id)
    return jsonify({
        "id" : result.id,
        "name" : result.name,
        "email" : result.email,
        "role" : result.role.value,
        "phone" : '' if result.phone is None else result.phone,
        "street" : '' if result.street is None else result.street,
        "city" :  '' if result.city is None else result.city,
        "province" : '' if result.province is None else result.province,
        "postal_code" : '' if result.postal_code is None else result.postal_code,
        "country" : '' if result.country is None else result.country
    }), 200

# GET by ID
@users_bp.route("/<int:user_id>", methods=["GET"])
@token_required
def get_user(user_id):
    result = Users.query.get_or_404(user_id)

    return jsonify({
        "id" : result.id,
        "name" : result.name,
        "email" : result.email,
        "role" : result.role.value,
        "phone" : result.phone,
        "street" : result.street,
        "city" :  result.citty,
        "province" : result.province,
        "postal_code" : result.postal_code,
        "country" : result.country
    }), 200


# Create new User
@users_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()

    print(data)
    if not data or "password" not in data or "email" not in data:
        return jsonify({"message" : "Invalid data"}), 400
    

    email = data["email"]

    user_exist = Users.query.filter_by(email=email).first()

    if user_exist:
        return jsonify({"message" : "Email already exist"}), 400
    
    try:
        new_user = Users(
            name = data["name"],
            email = data["email"],
            password = generate_password_hash(data["password"], "scrypt", 16),
            role = data["form_role"]
        )

        db.session.add(new_user)
        db.session.commit()

    except Exception as e:
        db.sesion.roll
        return jsonify({"message" : "Unexpected error occured"}), 400
    

    return jsonify({"message" : "User added"}), 200

# UPDATE USER
@users_bp.route("/<int:user_id>", methods=["PUT"])
@token_required
def update_user(current_user, user_id):
    user = Users.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({"message": "User not found"}), 400
    try:
        data = request.get_json()

        if not data:
            return jsonify({"message" : "No data found" }), 400

        if "name" in data:
            user.name = data["name"]

        if "form_role" in data:
            user.role = data["form_role"]

        if "phone" in data:
            user.phone = data["phone"]
        
        if "street" in data:
            user.street = data["street"]

        if "city" in data:
            user.city = data["city"]

        if "province" in data:
            user.province = data["province"]

        if "postal_code" in data:
            user.postal_code = data["postal_code"]

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


@users_bp.route("/search", methods=["GET"])
def search_user():
    query = request.args.get("q", "")

    if not query:
        return jsonify({"message": "Search query is required"}), 400
    
    results = Users.query.filter(Users.name.ilike(f"%{query}%")).all()

    return jsonify([
        {
            "id" : user.id,
            "name" : user.name,
            "email" : user.email,
            "role" : user.role.value
        }
        for user in results
    ]), 200