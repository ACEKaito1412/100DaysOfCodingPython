from flask  import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # add config
    app.config.from_object('app.configs.Config')

    # bind db to app
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # import blueprints
    from app.routes.orders import orders_bp
    from app.routes.products import products_bp
    from app.routes.users import users_bp

    app.register_blueprint(orders_bp, url_prefix='/api/orders')
    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(users_bp, url_prefix='/api/users')

    return app

