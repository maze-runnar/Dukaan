from flask_restful import Api
from app import flaskAppInstance
from .auth import AuthSignup, AuthLogin, MerchantSignup, MerchantLogin
# from .merchant_auth import MerchantSignup, MerchantLogin
from .user import UserDetail, MerchantDetail
from .item import ItemDetail, ItemPost

restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(AuthSignup,"/api/v1/auth")
restServerInstance.add_resource(AuthLogin,"/api/v1/login")
restServerInstance.add_resource(MerchantSignup,"/api/v1/merchant/auth")
restServerInstance.add_resource(MerchantLogin,"/api/v1/merchant/login")
restServerInstance.add_resource(UserDetail,"/api/v1/user/<userid>")
restServerInstance.add_resource(MerchantDetail,"/api/v1/merchant/<merchantid>")
restServerInstance.add_resource(ItemDetail,"/api/v1/item/<itemid>")
restServerInstance.add_resource(ItemPost,"/api/v1/item")
