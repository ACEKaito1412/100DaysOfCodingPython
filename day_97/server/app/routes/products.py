from flask import Blueprint, request, jsonify
from app.models.products import Product
from app import db
from app.utils import token_required

products_bp = Blueprint('products', __name__)

# GET ALL PRODUCTS
@products_bp.route('/', methods=['GET'])
def get_products():
    results = Product.query.all()
    return jsonify([
        {
            "id" : item.id,
            "name" : item.name,
            "description" : item.description,
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
            "description" : result.description,
            "price" : result.price,
            "stock" : result.stock
        }
    ), 200

#

@products_bp.route("/<int:product_id>", methods=["PUT"])
@token_required
def update_product(current_user, product_id):
    item = Product.query.filter_by(id=product_id).first()

    if not item:
        return jsonify({"error" : "Product not found"}), 401
    try:
        data = request.get_json()

        if "name" in data:
            item.name = data["name"]
        if "price" in data:
            item.price = data["price"]
        if "stock" in data:
            item.stock = data["stock"]
    except Exception as  e:
        return jsonify({"error" : f"{e}"}), 400 
    
    
    db.session.commit()

    return jsonify({
        "message" : "Product updated",
        "product" : {
            "id"    : item.id,
            "name"  : item.name,
            "description" : item.description,
            "price" : item.price,
            "stock" : item.stock
        }
    }), 200

# ADD NEW PRODUCT
@products_bp.route("/", methods = ["POST"])
@token_required
def create_product(current_user):
    data = request.get_json()

    if not data or "name" not in data or "price" not in data:
        return jsonify({"error" : "Invalid input"}), 400
    
    product = Product(
        name = data["name"],
        description = data["description"],
        price = data["price"],
        stock = data["stock"]
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message" : "Product added", "name" : product.name}), 200

# DELETE PRODCT
@products_bp.route("/<int:product_id>", methods=["DELETE"])
@token_required
def remove_product(current_user, product_id):
    result = Product.query.get_or_404(product_id)

    db.session.delete(result)
    db.session.commit()

    return jsonify({"message" : "Product deleted", "status" : 200})

# SEARCH PRODUCT 
@products_bp.route("/search", methods=["GET"])
def search_product():
    query = request.args.get("q", "")

 
    if not query:
        return jsonify({"error" : "Search query is required."}), 400
    
    results = Product.query.filter(Product.name.ilike(f"%{query}%")).all()

    return jsonify([
        {
            "id" : item.id,
            "name" : item.name,
            "description" : item.description,
            "price" : item.price,
            "stock" : item.stock
        } 
        for item in results
    ]), 200
    