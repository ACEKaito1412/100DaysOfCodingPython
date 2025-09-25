from flask  import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # add config
    app.config.from_object('app.configs.Config')

    # bind db to app
    db.init_app(app)

    # import blueprints
    from app.routes.orders import orders_bp
    from app.routes.products import products_bp
    from app.routes.users import users_bp
    from app.routes.auth import auth_bp
    from app.routes.cart import cart_bp
    from app.routes.payment import payment_bp

    app.register_blueprint(orders_bp, url_prefix='/api/orders')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(cart_bp, url_prefix='/api/carts')
    app.register_blueprint(payment_bp, url_prefix='/api/payment')

    return app

