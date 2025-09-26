import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = "secreto-keto"
    SQLALCHEMY_DATABASE_URI = "sqlite:///shop.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    PAYPAL_CLIENT = os.getenv('PAYPAL_CLIENT')
    PAYPAL_SECRET = os.getenv('PAYPAL_SECRET')
    PAYPAL_URI = "https://api-m.sandbox.paypal.com"