from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
from model.user import User, Merchant
from app import db

class UserDetail(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('location',
                                 type=str,
                                 location='json')
        self.parser.add_argument('pincode',
                                 type=str,
                                 location='json')
        self.parser.add_argument('bucket',
                                 type=str,
                                 location='json')
        self.parser.add_argument('personal_note',
                                 type=str,
                                 location='json')
        self.parser.add_argument('mobile',
                                 type=str,
                                 location='json')
        # self.parser.add_argument('favourites',
        #                          type=str,
        #                          location='json')
    
    user_fields = {
        'id': fields.Integer,
        'username': fields.String,
        'password_hash': fields.String,
        'location': fields.String,
        'pincode': fields.String,
        'bucket': fields.String,
        'personal_note': fields.String,
        'mobile': fields.String
    }

    @marshal_with(user_fields)
    def post(self, userid):
        logger.debug("Inside the post method of Task")
        pass


    def get(self, userid):
        logger.debug("Inisde the get method of Task")
        data = User.query.get(userid)
        # res = jsonify(data)
        # print("here is the response", make_response(jsonify(data)))
        return {
                    "data" : {
                                "username":data.username,
                                "location":data.location,
                                "pincode":data.pincode,
                                "bucket": data.bucket,
                                "personal_note":data.personal_note,
                                "mobile":data.mobile
                            }
                }

    def put(self, userid):
        logger.debug("Inisde the put method of Task")
        args = self.parser.parse_args()
        # print("args coming ...",args)
        data = User.query.get(userid)
        data.location = args["location"]
        data.pincode = args["pincode"]
        data.bucket = args["bucket"]
        data.personal_note = args["personal_note"]
        data.mobile = args["mobile"]
        db.session.commit()
        return {"data": str(data)},200

    def delete(sef, userid):

        logger.debug("Inisde the delete method of Task")   
        return {"message" : "user deleted"},200


class MerchantDetail(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('location',
                                 type=str,
                                 location='json')
        self.parser.add_argument('pincode',
                                 type=str,
                                 location='json')
        self.parser.add_argument('personal_note',
                                 type=str,
                                 location='json')
        self.parser.add_argument('mobile',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_verified',
                                 type=bool,
                                 location='json')
        
        # self.parser.add_argument('favourites',
        #                          type=str,
        #                          location='json')
    
    user_fields = {
        'id': fields.Integer,
        'username': fields.String,
        'password_hash': fields.String,
        'location': fields.String,
        'pincode': fields.String,
        'personal_note': fields.String,
        'mobile': fields.String,
        'is_verified': fields.Boolean
    }

    @marshal_with(user_fields)
    def post(self, merchantid):
        logger.debug("Inside the post method of Task")
        pass


    def get(self, merchantid):
        logger.debug("Inisde the get method of Task")
        data = Merchant.query.get(merchantid)
        # res = jsonify(data)
        # print("here is the response", make_response(jsonify(data)))
        print(data.items)
        items = []
        for i in data.items:
            d = {}
            d["name"] = i.name
            d["is_available"] = i.is_available
            items.append(d)
        return {
                    "data" : {
                                "username":data.username,
                                "location":data.location,
                                "pincode":data.pincode,
                                "personal_note":data.personal_note,
                                "mobile":data.mobile,
                                "is_verified":data.is_verified,
                                "items":items
                            }
                }

    def put(self, merchantid):
        logger.debug("Inisde the put method of Task")
        args = self.parser.parse_args()
        # print("args coming ...",args)
        data = Merchant.query.get(merchantid)
        data.location = args["location"]
        data.pincode = args["pincode"]
        data.personal_note = args["personal_note"]
        data.mobile = args["mobile"]
        try:
            db.session.commit()
            return {"data": str(data)},200
        except:
            return {"message": "some error occured"}

    def delete(sef, merchantid):

        logger.debug("Inisde the delete method of Task")   
        return {"message" : "user deleted"},200
