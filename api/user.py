from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
from model.user import User, Merchant
from app import db
from authy.api import AuthyApiClient

authy_api = AuthyApiClient('2M08EuvrYMMdyYIAjUaS85yaSqwJUArd')

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
                                "id": userid,
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
        print("updating user detail: ", args)
        data = User.query.get(userid)
        if "location" in args and (args["location"] != None):
            data.location = args["location"]
        if "pincode" in args and (args["pincode"] != None):
            print("coming in pincode args even if it's not")
            data.pincode = args["pincode"]
        if "bucket" in args and (args["bucket"] != None):
            data.bucket = args["bucket"]
        if "personal_note" in args and (args["personal_note"] != None):
            data.personal_note = args["personal_note"]
        if "mobile" in args and (args["mobile"] != None):
            data.mobile = args["mobile"]
        db.session.commit()
        return {"data": str("value updated successfully")},200

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
        return {
                    "data" : {
                                "username":data.username,
                                "location":data.location,
                                "pincode":data.pincode,
                                "personal_note":data.personal_note,
                                "mobile":data.mobile,
                                "is_verified":data.is_verified,
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


class VerifyMobile(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('mobile',
                                 type=str,
                                 default="",
                                 location='json')

    def post(self, merchantid):
        args = self.parser.parse_args()
        user = authy_api.users.create(
                email='dubesundaram99@gmail.com',
                phone=args["mobile"],
                country_code=91)
        if user.ok():
            data = Merchant.query.get(merchantid)
            data.authy_user_id = user.id
            try:
                db.session.commit()
                sms = authy_api.users.request_sms(user.id)
                if sms.ok():
                    return user.id
                else:
                    return {"msg": "sms not sent"}
            except:
                return {"msg": "something went wrong"}
            # user.id is the `authy_id` needed for future requests
        else:
            return user.errors()

class VerifyToken(Resource):
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('otp',
                                 type=str,
                                 default="",
                                 location='json')

    def post(self, merchantid):
        args = self.parser.parse_args()
        data = Merchant.query.get(merchantid)
        verification = authy_api.tokens.verify(data.authy_user_id, token=args["otp"])
        if(verification.ok()):
            data.is_verified = True
            try:
                db.session.commit()
                return {"msg": "user verified"}
            except:
                return {"msg": "something went wrong"}
        else:
            return {"msg": "otp is wrong"}