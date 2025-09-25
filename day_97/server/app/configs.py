

class Config:
    SECRET_KEY = "secreto-keto"
    SQLALCHEMY_DATABASE_URI = "sqlite:///shop.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    PAYPAL_CLIENT = "AcejfMHpFVPSv3rXuPny2wALrf_oos952FQlpc-jBwtn_oeSJOPEKeD0dPhFS-E09bb3cUXk10vqLtk_"
    PAYPAL_SECRET = "ED3HvGZj-vkaLk2PDGMPGUtFKvfZMQYYxaUwLnoVgEtfzktL_rZmndqL2BBSAUSea_ddYFWwha27yaOw"
    PAYPAL_URI = "https://api-m.sandbox.paypal.com"