from flask import Flask
import logging as logger
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from marshmallow_sqlalchemy import *
# from flask_marshmallow import *
from flask_cors import CORS


logger.basicConfig(level="DEBUG")


flaskAppInstance = Flask(__name__)

CORS(flaskAppInstance)

flaskAppInstance.config.from_object(Config)
db = SQLAlchemy(flaskAppInstance)
migrate = Migrate(flaskAppInstance, db)

from flask_restful import Api
from api.auth import AuthSignup, AuthLogin, MerchantSignup, MerchantLogin
# from .merchant_auth import MerchantSignup, MerchantLogin
from api.user import UserDetail, MerchantDetail, VerifyMobile, VerifyToken,UserNameFilterDetail
from api.item import ItemDetail, ItemPost, ItemList, ItemListByCategory
from api.notification import NotificationPost, NotificationDetail
from api.shop import NearShopList, ShopPost, ShopList, ShopDetail
from api.upload import ImageUpload
from api.khatabook import KhataPost, KhataList, KhataDetail

restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(AuthSignup,"/api/v1/user/auth")
restServerInstance.add_resource(AuthLogin,"/api/v1/user/login")
restServerInstance.add_resource(MerchantSignup,"/api/v1/merchant/auth")
restServerInstance.add_resource(MerchantLogin,"/api/v1/merchant/login")
restServerInstance.add_resource(UserDetail,"/api/v1/user/<userid>")
restServerInstance.add_resource(MerchantDetail,"/api/v1/merchant/<merchantid>")
restServerInstance.add_resource(ItemDetail,"/api/v1/item/<itemid>")
restServerInstance.add_resource(ItemPost,"/api/v1/shop/item/new")
restServerInstance.add_resource(ItemList,"/api/v1/shop/items/<shopid>")
restServerInstance.add_resource(VerifyMobile, "/api/v1/otp/<merchantid>")
restServerInstance.add_resource(VerifyToken, "/api/v1/verify/<merchantid>")
restServerInstance.add_resource(NotificationPost, "/api/v1/notification/new")
restServerInstance.add_resource(NotificationDetail, "/api/v1/notification/<merchantid>")
restServerInstance.add_resource(NearShopList, "/api/v1/shop/nearby/<userid>")
restServerInstance.add_resource(ShopPost, "/api/v1/merchant/shop/new")
restServerInstance.add_resource(ShopDetail, "/api/v1/shop/<shopid>")
restServerInstance.add_resource(ShopList, "/api/v1/merchant/shops/<merchantid>")
restServerInstance.add_resource(ImageUpload, "/api/v1/upload/image")
restServerInstance.add_resource(KhataPost, "/api/v1/khata/new")
restServerInstance.add_resource(KhataList, "/api/v1/shop/khata/<shopid>")
restServerInstance.add_resource(KhataDetail, "/api/v1/khata/<khataid>")
restServerInstance.add_resource(UserNameFilterDetail, "/api/v1/userdetail/filter")
restServerInstance.add_resource(ItemListByCategory, "/api/v1/item/category/filter") ##filter by category use like "/api/v1/item/category/filter?category=all&limit=50"
# ma = Marshmallow(flaskAppInstance)
db.create_all()

if __name__ == '__main__':

    logger.debug("Starting Flask Server")
    flaskAppInstance.run(host="127.0.0.1",port=5000,debug=True,use_reloader=True)