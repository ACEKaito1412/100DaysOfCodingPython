from flask import Blueprint, request, jsonify
from app.models.carts import CartItem, Cart
from app.utils import token_required
from app import db

cart_bp = Blueprint('cart', __name__)

# GET Cart BY user Auth
@cart_bp.route("/", methods=["GET"])
@token_required
def get_cart(current_user):

    cart = Cart.query.filter_by(user_id = current_user.id).first_or_404()

    sub_total = 0
    item_count = len(cart.items)
    shipping = 70

    for item in cart.items:
        sub_total += item.quantity * item.product.price

    return jsonify({
        "id" : cart.id,
        "user_id" : cart.user_id,
        "item_count" : item_count,
        "sub_total" : sub_total,
        "shipping" : shipping,
        "total" : round(shipping + sub_total,2),
        "items" : [
            {
                "id" : i.id,
                "product_id" : i.product_id, 
                "product_name" : i.product.name,
                "image_uri" : i.product.image_uri,
                "quantity" : i.quantity,
                "price" : i.product.price,
                "total" : round(i.product.price * i.quantity, 2)
            }
            for i in cart.items
            ]
        }), 200


# CREATE NEW cart
@cart_bp.route("/", methods=["POST"])
@token_required
def create_cart(current_user):
    data = request.get_json()

    if not data:
        return jsonify({"error" : "Invalid input"}), 400
    
    result_cart = Cart.query.filter_by(user_id = current_user.id).first()

    if result_cart:
        return jsonify({"message" : "cart already exist", "id" : result_cart.id}), 201
 

    cart = Cart(user_id = data["user_id"])
    db.session.add(cart)
    db.session.commit()

    return jsonify({"message" : "cart created", "id" : cart.id}), 201


# ADD ITEM TO CART
@cart_bp.route("/", methods=["PUT"])
@token_required
def add_to_cart(current_user):
    data = request.get_json()

    if not data or "user_id" not in data or "product_id" not in data:
        return jsonify({"message" : "Invalid input"}), 400
    
    if current_user.id != data["user_id"]:
        return jsonify({"message": "Encountered error while authenticating"}), 400
    
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    cart_item = CartItem(
        product_id = data["product_id"],
        quantity = 1,
        cart = cart
    )

    db.session.add(cart_item)
    db.session.add(cart)
    db.session.commit()

    return jsonify({"message" : "product added to cart", "id" : cart.id}), 201

# ADD ITEM TO CART
@cart_bp.route("/<int:cartitem_id>", methods=["PUT"])
@token_required
def update_cart(current_user, cartitem_id):
    data = request.get_json()

    if not data or "quantity" not in data:
        return jsonify({"error" : "Invalid input"}), 400
       
    quantity = data["quantity"]
    
    cart_item = CartItem.query.filter_by(id=cartitem_id).first()

    if quantity == 0:
        db.session.delete(cart_item)
    else:
        cart_item.quantity = quantity

    db.session.commit()

    return jsonify({"message" : "cart item updated", "id" : cart_item.id}), 201

# DELETE cart
@cart_bp.route("/<int:cart_id>", methods=["DELETE"])
def delete_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    db.session.delete(cart)
    db.session.commit()

    return jsonify({"message" : "cart deleted"}), 200

