from flask import Blueprint, render_template, request
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
    
    error = []

    if request.method == "POST":
        form_data = request.get_data()
        
        if not form_data or "name" not in form_data or "price" not in form_data:
            error.append("Missing important details.")

        if error == None:
            data = product_api.create(form_data)

    return render_template("products.html", data = data, error = error)