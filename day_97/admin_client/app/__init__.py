from flask import Flask, current_app
from app.service.api_client import ProductApi, AuthApi, UserApi
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

    # import blueprint
    from app.routes.dashboard import dashboard_bp
    from app.routes.login import login_bp
    from app.routes.product_management import product_bp

    # initialize routes

    app.register_blueprint(dashboard_bp, url_prefix="/dashboard/")
    app.register_blueprint(login_bp, url_prefix="/dashboard/login/")
    app.register_blueprint(product_bp, url_prefix="/dashboard/products/")

    return app