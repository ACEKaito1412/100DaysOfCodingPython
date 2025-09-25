from flask import Blueprint, render_template, session
from app.service.api_client import ProductApi
from app.util import login_required, is_login

product_api = None

shop_bp = Blueprint("shop", __name__)

def init_shop(product_client:ProductApi):
    global product_api
    product_api = product_client


@shop_bp.route("/", methods=["GET", "POST"])
def home():

    products = product_api.get_all()
    return render_template('main.html', data = products, is_login = is_login())