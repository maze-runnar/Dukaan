from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
# from model.item import Item
from model.user import User, Merchant
from app import db
from model.shop import Shop, ShopImages


class NearShopList(Resource):

    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('userid',
                                 type=int,
                                 location='json')

    def get(self, userid):
        logger.debug("Inisde the get method of Near BY shops")
        user = User.query.get(userid)
        user_pincode = user.pincode
        near_shops = []
        if user_pincode != "" or user_pincode != None:
            near_shops = Shop.query.filter_by(pincode=user_pincode).all()

        if "itemname" in request.args:
            itemname = request.args.get('itemname')
            limit = 50
            if request.args.get('limit'):
                limit = request.args.get('limit')
            if itemname != "":
                near_shops = Shop.query.filter(
                    Shop.name.ilike(f'%{itemname}%')).limit(limit).all()

        shops = []
        for i in near_shops:
            x = {
                "id": i.id,
                "name": i.name,
                "location": i.location,
                "mobile": i.mobile,
                "opening_time": i.opening_time,
                "close_time": i.closing_time

            }
            shops.append(x)

        # logger.debug("Merchants near me: ", merchants)

        return {"data": shops}


class ShopPost(Resource):
    def __init__(self):
        """Parse arguments from json"""
        self.parser = reqparse.RequestParser()

        self.parser.add_argument('name',
                                 type=str,
                                 location='json')
        self.parser.add_argument('home_delivery_available',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('created_at',
                                 type=str,
                                 location='json')
        self.parser.add_argument('pincode',
                                 type=str,
                                 location='json')
        self.parser.add_argument('mobile',
                                 type=str,
                                 location='json')
        self.parser.add_argument('location',
                                 type=str,
                                 location='json')
        self.parser.add_argument('closing_time',
                                 type=str,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('opening_time',
                                 type=str,
                                 location='json')

    def post(self):
        logger.debug("Inside the post method of Task SHOP POST")
        print(self)
        args = self.parser.parse_args()
        print("args coming ...", args)
        # print(name)
        shop = Shop(name=args["name"], home_delivery_available=args["home_delivery_available"], merchant_id=args["merchant_id"], created_at=args["created_at"],
                    pincode=args["pincode"], mobile=args["mobile"], location=args["location"], opening_time=args['opening_time'], closing_time=args['closing_time'], description=args['description'])
        # item.name = args["name"]
        # item.merchant_id = args["merchant_id"]
        db.session.add(shop)
        db.session.commit()
        return {
            "name": args["name"], "home_delivery_available": args["home_delivery_available"], "merchant_id": args["merchant_id"], "created_at": args["created_at"],
            "pincode": args["pincode"], "mobile": args["mobile"], "location": args["location"], "opening_time": args['opening_time'], "closing_time": args['closing_time'], "description": args['description']
        }


class ShopDetail(Resource):  # this is shop detail API

    def __init__(self):
        """Parse arguments from json"""
        self.parser = reqparse.RequestParser()

        self.parser.add_argument('name',
                                 type=str,
                                 location='json')
        self.parser.add_argument('home_delivery_available',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('created_at',
                                 type=str,
                                 location='json')
        self.parser.add_argument('pincode',
                                 type=str,
                                 location='json')
        self.parser.add_argument('mobile',
                                 type=str,
                                 location='json')
        self.parser.add_argument('location',
                                 type=str,
                                 location='json')
        self.parser.add_argument('closing_time',
                                 type=str,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('opening_time',
                                 type=str,
                                 location='json')

    def get(self, shopid):  # in this we fetch all detail of detail function, passing shopid in API
        logger.debug("Inisde the get method of Task")
        data = Shop.query.filter_by(id=shopid).first()
        # res = jsonify(data)
        # print("here is the response", make_response(jsonify(data)))
        print(data)
        items = []
        for i in data.items:
            d = {}
            d["name"] = i.name
            d["is_available"] = i.is_available
            items.append(d)

        images = []
        for i in data.images:
            d = {}
            d["title"] = i.title
            d["url"] = i.url
            images.append(d)

        return {
            "data": {
                "id": data.id,
                "name": data.name,
                "home_delivery_available": data.home_delivery_available,
                "merchant_id": data.merchant_id,
                "created_at": data.created_at,
                "items": items,
                "images": images,
                "pincode": data.pincode,
                "mobile": data.mobile,
                "location": data.location,
                "opening_time": data.opening_time,
                "closing_time": data.closing_time,
                "description": data.description
            }

        }  # all the details we are fetching in /api/v1/shop/id API , so we will access in frontend using these fields as home_delivery_available, merchant_id etc..

    def put(self, shopid):  # to update the details of any specific shop, this function is responsible, you will call the same API, just update method in frontend method = "PUT"
        logger.debug("Inisde the put method of Task")
        args = self.parser.parse_args()
        # print("args coming ...",args)
        data = Shop.query.get(shopid)
        data.name = args["name"]
        data.description = args["description"]
        data.pincode = args["pincode"]
        db.session.commit()
        return {"data": str(data)}, 200

    def delete(sef, shopid):

        Shop.query.filter_by(id=shopid).delete()
        db.session.commit()
        logger.debug("Inisde the delete method of Task shop delete")
        return {"message": "user deleted"}, 200


class ShopList(Resource):  # showing shop list for a merchant that's why will take merchantid in API

    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()

        self.parser.add_argument('name',
                                 type=str,
                                 location='json')
        self.parser.add_argument('home_delivery_available',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('created_at',
                                 type=str,
                                 location='json')
        self.parser.add_argument('pincode',
                                 type=str,
                                 location='json')
        self.parser.add_argument('mobile',
                                 type=str,
                                 location='json')
        self.parser.add_argument('location',
                                 type=str,
                                 location='json')
        self.parser.add_argument('closing_time',
                                 type=str,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('opening_time',
                                 type=str,
                                 location='json')

    def get(self, merchantid):
        logger.debug("Inisde the get method of Task")
        data = db.session.query(Shop).filter_by(merchant_id=merchantid).all()

        shops = []
        for i in data:
            x = {
                "id": i.id,
                "name": i.name,
                "description": i.description,
                "pincode": i.pincode,
                "mobile": i.mobile,
                "opening_time": i.opening_time,
                "closing_time": i.closing_time
            }

            shops.append(x)

        # list of shops, from here shops is array of dictionary
        return {"data": shops}


class ShopImagePost(Resource):
    def __init__(self):
        """Parse arguments from json"""
        self.parser = reqparse.RequestParser()

        self.parser.add_argument('title',
                                 type=str,
                                 location='json')
        self.parser.add_argument('shop_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('url',
                                 type=str,
                                 location='json')

    def post(self):
        logger.debug("Inside the post method of Task SHOP POST")
        print(self)
        args = self.parser.parse_args()
        print("args coming ...", args)
        # print(name)
        shop_image = ShopImages(
            title=args["title"], url=args["url"], shop_id=args["shop_id"])
        # item.name = args["name"]
        # item.merchant_id = args["merchant_id"]
        db.session.add(shop_image)
        db.session.commit()
        return {
            "url": args["url"]
        }
