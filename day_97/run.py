from app import create_app
from app import db
from app.models.users import Users
from app.models.orders import OrderItem, Orders
from app.models.products import Product
from app.models.carts import Cart, CartItem

app = create_app()

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True, host="0.0.0.0", port=5000)