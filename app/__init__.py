from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import jwt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app_ = Flask(__name__)
    app_.config.from_object('app.config.Config')
    db.init_app(app_)
    bcrypt.init_app(app_)

    from .auth.routes import auth_bp
    app_.register_blueprint(auth_bp, auth_prefix="")

    with app_.app_context():
        from app.models import User
        db.create_all()

    return app_
