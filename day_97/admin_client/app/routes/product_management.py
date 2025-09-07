from flask import Blueprint, render_template
from app.util import login_required
from app.service.api_client import ProductApi

product_bp = Blueprint("product", __name__)

product_api = None

def init_product(api_client:ProductApi):
    global product_api

    product_api = api_client

@product_bp.route("/", methods=["POST", "GET"])
@login_required
def product():
    data = product_api.get_all()
    return render_template("products.html", data = data)