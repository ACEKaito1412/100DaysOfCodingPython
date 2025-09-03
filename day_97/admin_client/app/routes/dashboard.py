from flask import Blueprint, render_template
from app.util import login_required

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/", methods=["POST", "GET"])
@login_required
def home():
    return render_template("index.html")