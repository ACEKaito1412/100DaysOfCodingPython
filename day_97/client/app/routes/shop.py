from flask import Blueprint, render_template
from app.service.api_client import ProductApi

product_api = None

shop_bp = Blueprint("shop", __name__)

def init_shop(product_client:ProductApi):
    global product_api
    product_api = product_client


@shop_bp.route("/", methods=["GET", "POST"])
def home():
    products = product_api.get_all()

    return render_template('main.html', data = products[:8])