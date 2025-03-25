from flask import request, jsonify, Blueprint
from app.auth.services import signup_user, login_user, get_user_by_id, get_all_users
from app.schemas import SignupSchema, UserSchema, LoginSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    """

    :return:
    """

    data = request.get_json()
    validated_data = SignupSchema().load(data)

    # username = validated_data['username']
    # email = validated_data['email']
    # password = validated_data['password']
    #
    # signup_user(username=username, password=password, email=email)
    result = signup_user(**validated_data)

    return UserSchema().dump(result), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """"""
    data = request.get_json()
    validated_data = LoginSchema().load(data)

    result = login_user(**validated_data)

    return UserSchema().dump(result), 200


@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """

    :return:
    """
    user_id = get_jwt_identity()
    result = get_user_by_id(user_id)
    return UserSchema().dump(result), 200


@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """

    :return:
    """
    user_id = get_jwt_identity()

    results = get_all_users(user_id)

    return UserSchema().dump(
        results, many=True), 200


@auth_bp.route('/users/<user_id>', methods=['GET'])
@jwt_required()
def get_user_by_user_id(user_id):
    """

    :return:
    """
    result = get_user_by_id(user_id)

    return UserSchema().dump(result), 200


