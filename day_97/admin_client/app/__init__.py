from flask import Flask, current_app
from app.service.api_client import ProductApi, AuthApi, UserApi, OrdersApi
from dotenv import load_dotenv
import os


load_dotenv()


def create_app():
    app = Flask(__name__)

    # add config
    app.config.from_object("app.config.Config")

    # api client
    auth_client = AuthApi(os.getenv("BASE_URI"))
    product_client = ProductApi(os.getenv("BASE_URI"))
    user_client = UserApi(os.getenv("BASE_URI"))
    order_client = OrdersApi(os.getenv("BASE_URI"))

    # import blueprint
    from app.routes.dashboard import dashboard_bp, init_dashboard
    from app.routes.login import login_bp, init_login
    from app.routes.product_management import product_bp, init_product
    from app.routes.user import user_bp, init_user
    from app.routes.orders import orders_bp, init_order

    # initialize routes
    init_login(auth_client)
    init_product(product_client)
    init_user(user_client)
    init_order(order_client)
    init_dashboard(user_client, order_client, product_client)

    app.register_blueprint(dashboard_bp, url_prefix="/dashboard/")
    app.register_blueprint(login_bp, url_prefix="/dashboard/login/")
    app.register_blueprint(product_bp, url_prefix="/dashboard/products/")
    app.register_blueprint(user_bp, url_prefix="/dashboard/users/")
    app.register_blueprint(orders_bp, url_prefix="/dashboard/orders/")



    

    return app