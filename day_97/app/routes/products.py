from flask import Blueprint, request, jsonify
from app.models.products import Product
from app import db

products_bp = Blueprint('products', __name__)

# GET ALL PRODUCTS
@products_bp.route('/', methods=['GET'])
def get_products():
    results = Product.query.all()
    return jsonify([
        {
            "id" : item.id,
            "name" : item.name,
            "price" : item.price,
            "stock" : item.stock
        } 
        for item in results
    ]), 200

# GET PRODUCT BY ID
@products_bp.route("/<int:product_id>", methods = ["GET"])
def get_product(product_id):
    result = Product.query.get_or_404(product_id)
    return jsonify(
        {
            "id" : result.id,
            "name" : result.name,
            "price" : result.price,
            "stock" : result.stock
        }
    ), 200

# ADD NEW PRODUCT
@products_bp.route("/", methods = ["POST"])
def create_product():
    data = request.get_json()

    if not data or "name" not in data or "price" not in data:
        return jsonify({"error" : "Invalid input"}), 400
    
    product = Product(
        name = data["name"],
        price = data["price"],
        stock = data["stock"]
    )

    db.session.add(product)
    db.session.commit(product)

    return jsonify({"message" : "Product added", "id" : product.id}), 200

# DELETE PRODCT
@products_bp.route("/<int:product_id>", methods=["DELETE"])
def remove_product(product_id):
    result = Product.query.get_or_404(product_id)

    db.session.remove(result)
    db.session.commit()

    return jsonify({"message" : "Product deleted"}), 200