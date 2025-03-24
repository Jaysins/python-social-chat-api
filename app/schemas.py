from marshmallow import Schema, fields, post_load


class SignupSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

    @post_load
    def post_load(self, data, **kwargs):
        data['username'] = data['username'].lower()
        data['email'] = data['email'].lower()
        return data

