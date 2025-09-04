from functools import wraps
from flask import request, jsonify, current_app
from app.models.users import Users
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"error" : "Token not found"}), 401
        
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms="HS256")
            current_user = Users.query.get(data["user_id"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error" : "Token expired"}), 401
        except Exception as e:
            return jsonify({"error" : "Invalid token"}), 401


        return f(current_user, *args, **kwargs)

    return decorated