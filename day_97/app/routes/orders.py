from flask import Blueprint, request, jsonify


orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST', 'GET'])
def orders():
    return 'ok'
