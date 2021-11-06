from flask_restful import Api
from app import flaskAppInstance
from .auth import AuthSignup, AuthLogin, MerchantSignup, MerchantLogin
# from .merchant_auth import MerchantSignup, MerchantLogin
from .user import UserDetail, MerchantDetail, VerifyMobile, VerifyToken
from .item import ItemDetail, ItemPost
from .notification import NotificationPost, NotificationDetail
from .shop import NearShopList

restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(AuthSignup,"/api/v1/auth")
restServerInstance.add_resource(AuthLogin,"/api/v1/login")
restServerInstance.add_resource(MerchantSignup,"/api/v1/merchant/auth")
restServerInstance.add_resource(MerchantLogin,"/api/v1/merchant/login")
restServerInstance.add_resource(UserDetail,"/api/v1/user/<userid>")
restServerInstance.add_resource(MerchantDetail,"/api/v1/merchant/<merchantid>")
restServerInstance.add_resource(ItemDetail,"/api/v1/item/<itemid>")
restServerInstance.add_resource(ItemPost,"/api/v1/item")
restServerInstance.add_resource(VerifyMobile, "/api/v1/otp/<merchantid>")
restServerInstance.add_resource(VerifyToken, "/api/v1/verify/<merchantid>")
restServerInstance.add_resource(NotificationPost, "/api/v1/notification")
restServerInstance.add_resource(NotificationDetail, "/api/v1/notification/<merchantid>")
restServerInstance.add_resource(NearShopList, "/api/v1/nearby/<userid>")
