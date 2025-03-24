from flask import request, jsonify, Blueprint
from app import db, bcrypt
from app.models import User
from app.schemas import SignupSchema

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    """

    :return:
    """

    data = request.get_json()
    validated_data = SignupSchema().load(data)

    username = validated_data['username']
    email = validated_data['email']
    password = validated_data['password']

    if User.query.filter_by(email=email).first():
        return jsonify({'message': "email already exist"}), 409

    hashed_password = bcrypt.generate_password_hash(password)

    new_user = User(username=username, email=email,
                    password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'message': 'User created',
        "username": new_user.username,
        "email": new_user.email,
        "id": new_user.id,
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """"""
