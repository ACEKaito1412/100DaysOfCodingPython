from flask import Blueprint, render_template, current_app, jsonify, session, request, redirect, url_for
from app.utils import token_required, get_access_token
import requests
from app.models.carts import Cart
from app import db
from app.routes.cart import CartStatus

payment_bp = Blueprint("payment", __name__)

BASE_URL = "https://api-m.sandbox.paypal.com"



def create_purchase_unit(cart:Cart, shipping_cost=0.0):
    total_item = sum(item.quantity * item.product.price for item in cart.items)
    total_amount = total_item + shipping_cost
    
    return {
        "reference_id" : cart.id,
        "amount": {
            "currency_code": "USD",
            "value": f"{total_amount:.2f}",
            "breakdown": {
                "item_total": {
                    "currency_code": "USD",
                    "value": f"{total_item:.2f}"
                },
                "shipping": {
                    "currency_code": "USD",
                    "value": f"{shipping_cost:.2f}"
                }
            }
        },
        "items" : [
            {
                "name" : item.product.name,
                "unit_amount" : {
                    "currency_code": "USD",
                    "value": item.product.price
                },
                "quantity" : item.quantity
            } for item in cart.items
        ]
    }

@payment_bp.route("/create-order/<int:cart_id>", methods=["POST"])
@token_required
def create_order(current_user, cart_id):
    access_token = get_access_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    cart = Cart.query.filter_by(id = cart_id, status = CartStatus.ACTIVE).one_or_none()

    purchase_units = create_purchase_unit(cart, 70)

    data = request.get_json()

    order_payload = {
        "intent": "CAPTURE",
        "purchase_units": [
            purchase_units
        ],
        "application_context": {
            "return_url": data["return_url"],
            "cancel_url": data["cancel_url"]
        },
        "payment_source": {
            "paypal": {
                "experience_context": {
                    "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
                    "payment_method_selected": "PAYPAL",
                    "user_action": "PAY_NOW"
                }
            }
        }
    }

    response = requests.post(f"{BASE_URL}/v2/checkout/orders", headers=headers, json=order_payload)
    order = response.json()

    # Get approval URL
    approve_url = order['links'][1]['href']

    print(approve_url)
    return jsonify({
        "url" : approve_url
        }), 200

@payment_bp.route("/capture-order")
def capture_order():
    data = request.get_json()

    order_id = data['token']
    cart_id = data['cart_id']

    access_token = get_access_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.post(f"{BASE_URL}/v2/checkout/orders/{order_id}/capture", headers=headers)
    capture = response.json()

    if capture.get("status") == "COMPLETED":
        cart = Cart.query.filter_by(id=cart_id).update({"status" : CartStatus.PAID, 'token_id' : order_id})
        db.session.commit()
        return jsonify({"message" : "Payment succesfull"})
    else:
        return jsonify({"message" : "Payment failed"})
    


@payment_bp.route("/cancel-order")
@token_required
def cancel_order():
    return "<h2>⚠️ Payment was cancelled by the user.</h2>"


