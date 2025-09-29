from flask import Blueprint, request, jsonify
from app.models.orders import OrderItem, Orders
from app.models.carts import Cart   
from app.utils import token_required
from app import db

orders_bp = Blueprint('orders', __name__)

# GET ALL ORDERS
@orders_bp.route('/', methods=["GET"])
def get_orders():
    carts = Cart.query.filter_by(status='paid').all()

    if not carts:
        return jsonify({"message": "no orders yet", "status": 404}), 404

    response = []
    for cart in carts:
        sub_total = sum(item.quantity * item.product.price for item in cart.items)
        item_count = len(cart.items)
        shipping = 70
        total = round(sub_total + shipping, 2)

        response.append({
            "id": cart.id,
            "user_name": cart.user.name,
            "item_count": item_count,
            "sub_total": sub_total,
            "shipping": shipping,
            "total": total,
            "status": cart.status,
            "token_id" : cart.token_id, 
            "items": [
                {
                    "id": i.id,
                    "product_id": i.product_id,
                    "product_name": i.product.name,
                    "image_uri": i.product.image_uri,
                    "quantity": i.quantity,
                    "price": i.product.price,
                    "total": round(i.product.price * i.quantity, 2),
                }
                for i in cart.items
            ],
        })

    return jsonify(response), 200


# GET ORDER BY ID
@orders_bp.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = Orders.query.get_or_404(order_id)
    return jsonify({
        "id" : order.id,
        "user_id" : order.user_id,
        "items" : [
            {"product_id" : i.product_id, "quantity" : i.quantity}
            for i in order.items
        ]
    }), 200


# CREATE NEW ORDER
@orders_bp.route("/", methods=["POST"])
@token_required
def create_order(current_user):
    data = request.get_json()

    if not data or "user_id" not in data or "items" not in data:
        return jsonify({"error" : "Invalid input"}), 400
    
    if current_user.id != data["user_id"]:
        return jsonify({"message": "Encountered error while authenticating"}), 400
    
    order = Orders(user_id = data["user_id"])
    for item in data["items"]:
        order_item = OrderItem(
            product_id = item["product_id"],
            quantity = item["quantity", 1],
            order = order
        )

        db.session.add(order_item)

    db.session.add(order)
    db.session.commit()

    return jsonify({"message" : "Order created", "id" : order.id}), 201

# DELETE ORDER
@orders_bp.route("/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = Orders.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()

    return jsonify({"message" : "Order deleted"}), 200