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
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
    
    

    def post(self):
        logger.debug("Inside the post method of Task")
        args = self.parser.parse_args()
        print("args coming ...",args)
        # print(name)
        item = Item(name=args["name"], is_available=args["is_available"], merchant_id=args["merchant_id"])
        # item.name = args["name"]
        # item.merchant_id = args["merchant_id"]
        db.session.add(item)
        db.session.commit()
        return {"name":args["name"], "is_available":args["is_available"], "merchant_id":args["merchant_id"]}





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
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        
        # self.parser.add_argument('favourites',
        #                          type=str,
        #                          location='json')
    
    

    
    def get(self, itemid):
        logger.debug("Inisde the get method of Task")
        data = Item.query.get(itemid)
        # res = jsonify(data)
        # print("here is the response", make_response(jsonify(data)))
        return {
                    "data" : {
                                "name":data.name,
                                "is_available":data.is_available,
                                "merchant_id":data.merchant_id
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

