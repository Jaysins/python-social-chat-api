from ..models import User, db
from app import bcrypt
from flask_jwt_extended import create_access_token


def signup_user(username, email, password):
    hashed_password = bcrypt.generate_password_hash(password)

    new_user = User(username=username, email=email,
                    password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return new_user


def login_user(username, password):
    """

    :param username:
    :param password:
    :return:
    """

    user = User.query.filter_by(
        username=username.lower()).first()
    if not bcrypt.check_password_hash(
            user.password,
            password):
        raise ValueError('Password not correct')

    user.auth_token = create_access_token(
        user.id)

    return user


def get_user_by_id(user_id):
    return User.query.get(user_id)


def get_all_users(user_id):
    return User.query.filter(
        User.id != user_id).all()

