from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt
from flask_login import bcrypt, LoginManager
from flask_mail import Mail
from config import Config
from flask_mail import Message
from app import bcrypt
import smtplib


db = SQLAlchemy()
bcrypt = bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app