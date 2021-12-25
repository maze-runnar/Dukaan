from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
# from model.item import Item
from model.user import User, Merchant
from app import db
from model.shop import Shop


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
        shops = []
        for i in near_shops:
            x = {
                "id": i.id,
                "location": i.location,
                "mobile": i.mobile
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
                    "name":args["name"], "home_delivery_available":args["home_delivery_available"], "merchant_id":args["merchant_id"], "created_at":args["created_at"],
                    "pincode":args["pincode"], "mobile":args["mobile"], "location":args["location"], "opening_time":args['opening_time'], "closing_time":args['closing_time'], "description":args['description']
                }


class ShopDetail(Resource):

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
    def get(self, shopid):
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
        
        return {
            "data": {
                    "id": data.id,"name":data.name, "home_delivery_available": data.home_delivery_available, "merchant_id": data.merchant_id, "created_at": data.created_at, "items": items,
                    "pincode": data.pincode, "mobile": data.mobile, "location": data.location, "opening_time": data.opening_time, "closing_time": data.closing_time, "description": data.description
                }

        }

    def put(self, shopid):
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


class ShopList(Resource):

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
                "mobile": i.mobile
            }

            shops.append(x)

        return {"data": shops}
