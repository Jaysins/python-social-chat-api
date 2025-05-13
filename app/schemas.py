from marshmallow import Schema, fields, post_load, validates, ValidationError
from .models import User


class LoginSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)

    @validates("email")
    def validate_email(self, email):
        if not User.query.filter_by(email=email.lower()).first():
            raise ValidationError('email does not exist')


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
    friendStatus = fields.String(allow_none=True,
                                 required=False)


class LoginResponseSchema(Schema):
    user = fields.Nested(UserSchema, required=True,
                         allow_none=False)
    token = fields.String(allow_none=False,
                          required=True)
