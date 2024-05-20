import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('PAYMENT_DATABASE_URI', 'sqlite:///payments.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
