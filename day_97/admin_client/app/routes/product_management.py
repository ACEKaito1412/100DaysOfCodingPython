from flask import Blueprint, render_template
from app.util import login_required

product_bp = Blueprint("product", __name__)

@product_bp.route("", method=["POST", "GET"])
@login_required
def product():
    return render_template("products.html")