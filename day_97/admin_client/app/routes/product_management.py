from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from app.util import login_required
from app.service.api_client import ProductApi

product_bp = Blueprint("product", __name__)

product_api = None

def init_product(api_client:ProductApi):
    global product_api
    product_api = api_client

@product_bp.route("/", methods=["POST", "GET"])
@login_required
def home():
    product_api.set_token(session["token"])
    
    if request.method == "POST":
        form_data = request.form

        if not form_data or "name" not in form_data or "price" not in form_data:
            flash("Missing important details.", "error")
        elif "id" not in form_data:   
            res = product_api.create(form_data.to_dict())
        else:
            id = form_data["id"]
            res = product_api.update(form_data.to_dict(), id)

    
    data = product_api.get_all()
    return render_template("products.html", data = data, navigation=True)

@product_bp.route("/delete/<int:product_id>", methods=['GET'])
@login_required
def delete(product_id):
    result = product_api.delete(product_id)

    if result["status"] == 200:
        flash("Product deleted successfully ✅", "success")
    elif result["status"] == 400:
        flash("Item not found ❌", "error")
    else:
        flash("Something went wrong. Please try again.", "error")

    return redirect(url_for("product.product"))


@product_bp.route("/search", methods=["GET"])
@login_required
def search():
    q = request.args.get("q", "").lower()

    if q == "" or q == " ":
        res = product_api.get_all()
    else:   
        res = product_api.search(q)

    return render_template("_products.html", data = res)
