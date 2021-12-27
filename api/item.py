from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
from model.item import Item
from app import db

class ItemPost(Resource):
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_available',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('shop_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('max_order_amount',
                                 type=str,
                                 location='json')
        self.parser.add_argument('min_order_amount',
                                 type=str,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_deleted',
                                 type=bool,
                                 location='json')
        

    def post(self):
        logger.debug("Inside the post method of Task")
        args = self.parser.parse_args()
        print("args coming ...",args)
        # print(name)
        item = Item(name=args["name"], is_available=args["is_available"], shop_id=args["shop_id"],max_order_amount=args["max_order_amount"], min_order_amount=args["min_order_amount"], description=args["description"])
        # item.name = args["name"]
        # item.merchant_id = args["merchant_id"]
        db.session.add(item)
        db.session.commit()
        return {"name":args["name"], "is_available":args["is_available"], "shop_id":args["shop_id"]}





class ItemDetail(Resource):

    
    def __init__(self):
        """Parse arguments from json"""


        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_available',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('shop_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('max_order_amount',
                                 type=str,
                                 location='json')
        self.parser.add_argument('min_order_amount',
                                 type=str,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_deleted',
                                 type=bool,
                                 location='json')
        
    

    
    def get(self, itemid):
        logger.debug("Inisde the get method of Task")
        data = Item.query.get(itemid)
        # res = jsonify(data)
        # print("here is the response", make_response(jsonify(data)))
        return {
                    "data" : {
                                "name":data.name,
                                "is_available":data.is_available,
                                "shop_id":data.shop_id,
                                "description": data.description,
                                "max_order_amount": data.max_order_amount,
                                "min_order_amount": data.min_order_amount
                            }
                }

    def put(self, itemid):
        logger.debug("Inisde the put method of Task")
        args = self.parser.parse_args()
        # print("args coming ...",args)
        data = Item.query.get(itemid)
        data.is_available = args["is_available"]
        db.session.commit()
        return {"data": str(data)},200

    def delete(sef, itemid):

        logger.debug("Inisde the delete method of Task")   
        return {"message" : "user deleted"},200



class ItemList(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_available',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('shop_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('max_order_amount',
                                 type=str,
                                 location='json')
        self.parser.add_argument('min_order_amount',
                                 type=str,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_deleted',
                                 type=bool,
                                 location='json')
        

    
    def get(self, shopid):
        logger.debug("Inisde the get method of Task")
        data = db.session.query(Item).filter_by(shop_id=shopid).all()
        
        items = []
        for i in data:
            x = {
                    "name":i.name,
                    "is_available":i.is_available,
                    "shop_id":i.shop_id,
                    "description": i.description
                }
    
            items.append(x)

        return {"data": items}
