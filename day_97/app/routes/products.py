from flask import Blueprint, request, jsonify

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['POST', 'GET'])
def products():
    return 'ok products'