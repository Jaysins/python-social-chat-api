from flask import Blueprint
from app.auth.services import get_user_by_id, get_all_users
from app.schemas import UserSchema
from flask_jwt_extended import jwt_required, \
    get_jwt_identity

from app.utils import success_response

user_bp = Blueprint('users', __name__)


@user_bp.route('/all', methods=['GET'])
@jwt_required()
def get_users():
    """

    :return:
    """
    user_id = get_jwt_identity()

    results = get_all_users(user_id)

    response = UserSchema().dump(results, many=True)
    return success_response(
        message="Users fetched successfully",
        data=response,
        status_code=201
    )


@user_bp.route('/<user_id>', methods=['GET'])
@jwt_required()
def get_user_by_user_id(user_id):
    """

    :return:
    """
    result = get_user_by_id(user_id)

    return UserSchema().dump(result), 200
