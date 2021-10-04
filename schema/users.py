from model.user import User, Merchant
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field,SQLAlchemyAutoSchema


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

user_schema = UserSchema()

    # id = ma.auto_field()
    # username = ma.auto_field()
    # password_hash = ma.auto_field()
    # location = ma.auto_field()
    # bucket = ma.auto_field()
    # personal_note = ma.auto_field()
    # favourites = ma.auto_field()
    # is_verified = ma.auto_field()

class MerchantSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Merchant
        load_instance = True

merchant_schema = MerchantSchema()