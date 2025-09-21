from flask import Blueprint, render_template
from app.service.api_client import OrdersApi

orders_api = None

orders_bp = Blueprint("orders", __name__)


def init_order(orders_client:OrdersApi):
    global orders_api
    orders_api = orders_client

@orders_bp.route("/", methods=["GET", "POST"])
def home():
    orders = orders_api.get_all()    

    return render_template("orders.html", data = orders, navigation = True)  