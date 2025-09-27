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

    if "status" in result:
        if result['status'] == 402 or result['status'] == 403:
            return redirect(url_for('login.log_out'))
        elif result['status'] == 404:
            return render_template("cart.html", data = [], is_login = is_login())
    else:
        return render_template("cart.html", data = result, is_login = is_login())


@cart_bp.route("/add_cart/<int:product_id>")
@login_required
def add_item_cart(product_id):
    cart_api.set_token(session['token'])

    data = {"product_id" : product_id}

    result = cart_api.add_item(data)

    return redirect(url_for('cart.home'))

@cart_bp.route("/update/<int:item_id>", methods=["GET"])
@login_required
def update_cart(item_id):
    cart_api.set_token(session["token"])

    q = request.args.get("quantity", "").lower()

    if q != "" or q != " ":  
        data = {"product_id" : item_id, "quantity" : q}
        res = cart_api.add_item(data=data)

    result = cart_api.get_by_id()

    return render_template("_shopping_cart.html", data = result)

@cart_bp.route("/pay_cart/<int:cart_id>")
@login_required
def pay_cart(cart_id):
    payment_api.set_token(session["token"])

    data = {"return_url" : url_for('cart.success', cart_id=cart_id, _external = True), "cancel_url" : url_for('cart.cancelled', _external = True)}
    result = payment_api.create_order(cart_id, data)
    
    return redirect(result["url"])


@cart_bp.route("/success/<int:cart_id>")
@login_required
def success(cart_id):
    payment_api.set_token(session['token'])
    
    data = {
        "token" : request.args.get("token"),
        "payer_id" : request.args.get("PayerID"),
        "cart_id" : cart_id
    }

    result = payment_api.capture_order(data)

    print(result)
    return "success"

@cart_bp.route("/cancelled")
@login_required
def cancelled():
    return "cancelled"