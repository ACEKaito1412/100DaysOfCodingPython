from flask import Blueprint, render_template
from app.util import login_required
from app.service.api_client import OrdersApi, UserApi, ProductApi


user_client = None
order_client = None
product_client = None

dashboard_bp = Blueprint("dashboard", __name__)

def init_dashboard(user_api:UserApi, order_api:OrdersApi, product_api:ProductApi):
    global user_client, order_client, product_client
    user_client = user_api
    order_client = order_api
    product_client = product_api

@dashboard_bp.route("/", methods=["POST", "GET"])
@login_required
def home():

    res_user = user_client.get_all()
    res_order = order_client.get_all()
    res_product = product_client.get_all()

    data = {
        "user_count" : len(res_user),
        "order_count" : len(res_order), 
        "product_count" : len(res_product),
        "stock_count" : sum(item['stock'] or 0 for item in res_product),
        "lowest_stock" : [item for item in res_product if item['stock'] < 2 ]
    }

    return render_template("index.html", data = data, navigation=True)