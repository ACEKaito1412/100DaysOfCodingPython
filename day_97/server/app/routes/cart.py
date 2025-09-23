from flask import Blueprint, request, jsonify
from app.models.carts import CartItem, Cart
from app.utils import token_required
from app import db

cart_bp = Blueprint('cart', __name__)

# GET ALL cart
@cart_bp.route('/', methods=["GET"])
def get_cart():
    cart = Cart.query.all()

    return jsonify([
        {
            "id" : o.id,
            "user_id" : o.user_id,
            "items" : [
                {"product_id" : i.product_id, "quantity" : i.quantity}
                for i in o.items
            ]
        }
        for o in cart
    ]), 200

# GET cart BY ID
@cart_bp.route("/<int:cart_id>", methods=["GET"])
def get_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    return jsonify({
        "id" : cart.id,
        "user_id" : cart.user_id,
        "items" : [
            {"product_id" : i.product_id, "quantity" : i.quantity}
            for i in cart.items
        ]
    }), 200


# CREATE NEW cart
@cart_bp.route("/", methods=["POST"])
@token_required
def create_cart(current_user):
    data = request.get_json()

    if not data or "user_id" not in data or "items" not in data:
        return jsonify({"error" : "Invalid input"}), 400
    
    if current_user.id != data["user_id"]:
        return jsonify({"message": "Encountered error while authenticating"}), 400
    
    cart = cart(user_id = data["user_id"])
    for item in data["items"]:
        cart_item = CartItem(
            product_id = item["product_id"],
            quantity = item["quantity", 1],
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

