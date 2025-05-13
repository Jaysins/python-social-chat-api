from flask import request, Blueprint
from app.auth.services import signup_user, \
    login_user, \
    get_user_by_id, \
    get_all_users
from app.schemas import SignupSchema, \
    UserSchema, \
    LoginSchema, LoginResponseSchema
from flask_jwt_extended import jwt_required, \
    get_jwt_identity

from app.utils import success_response

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    """

    :return:
    """

    data = request.get_json()
    validated_data = SignupSchema().load(data)
    result = signup_user(**validated_data)
    response = UserSchema().dump(result)
    return success_response(
        message="User signed up successfully",
        data=response,
        status_code=201
    )


@auth_bp.route('/login', methods=['POST'])
def login():
    """"""
    data = request.get_json()
    validated_data = LoginSchema().load(data)

    result = login_user(**validated_data)
    response = LoginResponseSchema().dump(result)
    return success_response(
        message="User logged in successfully",
        data=response,
        status_code=201
    )


@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """

    :return:
    """
    user_id = get_jwt_identity()
    result = get_user_by_id(user_id)
    response = UserSchema().dump(result)
    return success_response(
        message="User profile fetched successfully",
        data=response,
        status_code=201
    )


@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """

    :return:
    """
    user_id = get_jwt_identity()

    results = get_all_users(user_id)

    response = UserSchema().dump(results)
    return success_response(
        message="Users fetched successfully",
        data=response,
        status_code=201
    )


@auth_bp.route('/users/<user_id>', methods=['GET'])
@jwt_required()
def get_user_by_user_id(user_id):
    """

    :return:
    """
    result = get_user_by_id(user_id)

    return UserSchema().dump(result), 200
