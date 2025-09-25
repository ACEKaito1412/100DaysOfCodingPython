from flask import Blueprint, render_template, current_app, jsonify, session, request, redirect, url_for
from app.service.api_client import CartApi, PaymentApi
from app.util import login_required, is_login
import base64, requests

cart_api = None
payment_api = None

cart_bp = Blueprint("cart", __name__)


def init_cart(cart_client:CartApi, payment_client:PaymentApi):
    global cart_api, payment_api
    cart_api = cart_client
    payment_api = payment_client

@cart_bp.route("/", methods=["GET", "POST"])
@login_required
def home():
    cart_api.set_token(session["token"])

    result = cart_api.get_by_id()

    return render_template("cart.html", data = result, is_login = is_login(), client_id = current_app.config['PAYPAL_CLIENT'])


@cart_bp.route("/update/<int:item_id>", methods=["GET"])
@login_required
def update_cart(item_id):
    cart_api.set_token(session["token"])

    q = request.args.get("quantity", "").lower()

    if q != "" or q != " ":  
        res = cart_api.update(cart_id=item_id, data={"quantity" : q})

    result = cart_api.get_by_id()

    return render_template("_shopping_cart.html", data = result, client_id = current_app.config['PAYPAL_CLIENT'])

@cart_bp.route("/pay_cart/<int:cart_id>")
@login_required
def pay_cart(cart_id):
    payment_api.set_token(session["token"])

    data = {"return_url" : url_for('cart.success', _external = True), "cancel_url" : url_for('cart.cancelled', _external = True)}
    result = payment_api.create_order(cart_id, data)
    
    return redirect(result["url"])


@cart_bp.route("/success")
@login_required
def success():
    payment_api.set_token(session['token'])
    
    data = {
        "token" : request.args.get("token"),
        "payer_id" : request.args.get("PayerID")
    }

    result = payment_api.capture_order(data)

    print(result)
    return "success"

@cart_bp.route("/cancelled")
@login_required
def cancelled():
    return "cancelled"