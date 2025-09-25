from functools import wraps
from flask import request, jsonify, current_app
from app.models.users import Users
import jwt, base64, requests

def get_access_token():
    auth = base64.b64encode(f"{current_app.config['PAYPAL_CLIENT']}:{current_app.config['PAYPAL_SECRET']}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    data = {"grant_type": "client_credentials"}
    res = requests.post(f"{current_app.config['PAYPAL_URI']}/v1/oauth2/token", headers=headers, data=data)
    return res.json()["access_token"]

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"message" : "Token not found", "status" : 401}), 401
        
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms="HS256")
            current_user = Users.query.get(data["user_id"])
        except jwt.ExpiredSignatureError:
            return jsonify({"message" : "Token expired", "status" : 402}), 402
        except Exception as e:
            return jsonify({"message" : "Invalid token", "status" : 403}), 403

        return f(current_user, *args, **kwargs)

    return decorated