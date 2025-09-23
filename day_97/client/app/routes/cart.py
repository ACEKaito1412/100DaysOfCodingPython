from flask import Blueprint, render_template, current_app, jsonify
from app.service.api_client import CartApi
from app.util import login_required, is_login
import base64, requests

cart_api = None

cart_bp = Blueprint("cart", __name__)

BASE_URL = "https://api-m.sandbox.paypal.com"

def init_cart(cart_client:CartApi):
    global cart_api
    cart_api = cart_client


def get_access_token():
    auth = base64.b64encode(f"{current_app.config['PAYPAL_CLIENT']}:{current_app.config['PAYPAL_SECRET']}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    data = {"grant_type": "client_credentials"}
    res = requests.post(f"{BASE_URL}/v1/oauth2/token", headers=headers, data=data)
    return res.json()["access_token"]

@cart_bp.route("/", methods=["GET", "POST"])
@login_required
def home():

    return render_template("cart.html", is_login = is_login(), client_id = current_app.config['PAYPAL_CLIENT'])


@cart_bp.route("/create-order", methods=["POST"])
@login_required
def create_order():
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

    order_data = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {"currency_code": "USD", "value": "20.00"},
            "description": "Custom T-shirt"
        }]
    }

    res = requests.post(f"{BASE_URL}/v2/checkout/orders", headers=headers, json=order_data)
    return jsonify(res.json())

@cart_bp.route("/capture-order/<order_id>", methods=["POST"])
def capture_order(order_id):
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    res = requests.post(f"{BASE_URL}/v2/checkout/orders/{order_id}/capture", headers=headers)
    return jsonify(res.json())
