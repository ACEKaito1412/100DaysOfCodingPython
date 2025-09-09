from flask import Blueprint, render_template, request, session
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
    product_api.set_token(session["token"])

    error = []

    if request.method == "POST":
        form_data = request.form


        if not form_data or "name" not in form_data or "price" not in form_data:
            error.append("Missing important details.")

        if len(error) == 0:
            if "id" not in form_data:   
                res = product_api.create(form_data.to_dict())
            else:
                id = form_data["id"]
                print(form_data.to_dict())
                res = product_api.update(form_data.to_dict(), id)

    data = product_api.get_all()
    
    return render_template("products.html", data = data, error = error)