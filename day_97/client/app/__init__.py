from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():

    app = Flask(__name__)

    from app.routes.shop import shop_bp, init_shop
    from app.routes.login import login_bp, init_login
    from app.routes.signup import signup_bp, init_signup

    from app.service.api_client import ProductApi
    from app.service.api_client import AuthApi
    from app.service.api_client import UserApi

    product_api = ProductApi(os.getenv("BASE_URI"))
    auth_api = AuthApi(os.getenv("BASE_URI"))
    user_api = UserApi(os.getenv("BASE_URI"))

    init_shop(product_api)
    init_login(auth_api)
    init_signup(user_api)

    app.register_blueprint(shop_bp)
    app.register_blueprint(login_bp, url_prefix="/login/")
    app.register_blueprint(signup_bp, url_prefix="/signup/")

    return app

