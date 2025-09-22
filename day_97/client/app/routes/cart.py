from flask import Blueprint, render_template
from app.service.api_client import CartApi

cart_api = None

cart_bp = Blueprint("cart", __name__)

def init_cart(cart_client:CartApi):
    global cart_api
    cart_api = cart_client

@cart_bp.route("/", methods=["GET", "POST"])
def home():
    return render_template("cart.html")

