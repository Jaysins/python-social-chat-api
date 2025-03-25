from marshmallow import Schema, fields, post_load, validates, ValidationError
from .models import User


class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    @validates("username")
    def validate_username(self, username):
        if not User.query.filter_by(username=username.lower()).first():
            raise ValidationError('username does not exist')


class SignupSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

    @post_load
    def post_load(self, data, **kwargs):
        data['username'] = data['username'].lower()
        data['email'] = data['email'].lower()
        return data

    @validates('email')
    def validate_email(self, email):
        """

        :param email:
        :return:
        """
        if User.query.filter_by(email=email.lower()).first():
            raise ValidationError('email already exists')


class UserSchema(Schema):
    username = fields.String()
    email = fields.String()
    bio = fields.String(allow_none=True,
                        required=False)
    location = fields.String(allow_none=True,
                             required=False)
    id = fields.String()
    picture = fields.String(allow_none=True,
                            required=False)
    auth_token = fields.String(allow_none=True,
                               required=False)
