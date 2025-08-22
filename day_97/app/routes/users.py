from flask import Blueprint, request, jsonify

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST', 'GET'])
def users():
    return 'ok users'