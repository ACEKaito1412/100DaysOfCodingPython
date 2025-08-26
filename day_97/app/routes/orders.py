from flask import Blueprint, request, jsonify
from app.models.orders import OrderItem, Orders
from app import db

orders_bp = Blueprint('orders', __name__)

# GET ALL ORDERS
@orders_bp.route('/', methods=["GET"])
def get_orders():
    orders = Orders.query.all()

    return jsonify([
        {
            "id" : o.id,
            "user_id" : o.user_id,
            "items" : [
                {"product_id" : i.product_id, "quantity" : i.quantity}
                for i in o.items
            ]
        }
        for o in orders
    ]), 200

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
def create_order():
    data = request.get_json()

    if not data or "user_id" not in data or "items" not in data:
        return jsonify({"error" : "Invalid input"}), 400
    
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