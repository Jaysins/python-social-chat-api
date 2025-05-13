from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()


def create_app():
    app_ = Flask(__name__)
    app_.config.from_object('app.config.Config')
    db.init_app(app_)
    bcrypt.init_app(app_)
    jwt.init_app(app_)
    cors.init_app(app_)

    from .auth.routes import auth_bp
    from .user.routes import user_bp
    app_.register_blueprint(auth_bp, url_prefix="/api/auth")
    app_.register_blueprint(user_bp, url_prefix="/api/users")

    return app_