from flask import Flask

def create_app():
    app = Flask(__name__)


    # add config
    # app.config.from_object("app.config.Config")

    # import blueprint
    from app.routes.dashboard import dashboard_bp
    from app.routes.login import login_bp
    from app.routes.product_management import product_bp

    app.register_blueprint(dashboard_bp, url_prefix="/dashboard/")
    app.register_blueprint(login_bp, url_prefix="/dashboard/login/")
    app.register_blueprint(product_bp, url_prefix="/dashboard/products/")

    return app