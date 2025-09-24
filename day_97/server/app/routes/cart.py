from flask import Blueprint, request, jsonify
from app.models.carts import CartItem, Cart
from app.utils import token_required
from app import db

cart_bp = Blueprint('cart', __name__)


# GET cart BY ID
@cart_bp.route("/", methods=["GET"])
@token_required
def get_cart(current_user):
    cart = Cart.query.filter_by(user_id = current_user.id).first()
    print("hello")
    return jsonify({
        "id" : cart.id,
        "user_id" : cart.user_id,
        "items" : [
            {
                "product_id" : i.product_id, 
                "name" : i.product.name,
                "description" : i.product.description,
                "image_uri" : i.product.image_uri,
                "quantity" : i.quantity,
                "price" : i.product.price,
                "total" : i.product.price * i.quantity
            }
            for i in cart.items
        ]
    }), 200


# ADD to cart
@cart_bp.route("/", methods=["POST"])
@token_required
def create_cart(current_user):
    data = request.get_json()

    if not data or "user_id" not in data or "product_id" not in data:
        return jsonify({"error" : "Invalid input"}), 400
    

    if current_user.id != data["user_id"]:
        return jsonify({"message": "Encountered error while authenticating"}), 400
    
    cart = Cart(user_id = data["user_id"])

    cart_item = CartItem(
        product_id = data["product_id"],
        quantity = data["quantity"],
        cart = cart
    )

    db.session.add(cart_item)
    db.session.add(cart)
    db.session.commit()

    return jsonify({"message" : "cart created", "id" : cart.id}), 201

# DELETE cart
@cart_bp.route("/<int:cart_id>", methods=["DELETE"])
def delete_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    db.session.delete(cart)
    db.session.commit()

    return jsonify({"message" : "cart deleted"}), 200

