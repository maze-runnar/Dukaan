from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for
from model.user import User, Merchant
from app import db
import hashlib

class AuthSignup(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',
                                 type=str,
                                 required=True,
                                 help='No name provided',
                                 location='json')
        self.parser.add_argument('password_hash',
                                 type=str,
                                 default="",
                                 location='json')
    user_fields = {
        'id': fields.Integer,
        'username': fields.String,
        'password_hash': fields.String
    }

    def post(self):
        logger.debug("Inside the post method of Task")
        args = self.parser.parse_args()
        print(args)
        try:
            password = hashlib.sha256((args["password_hash"]).encode())
            password = password.hexdigest()
            print("what is the password - ", password)
            user = User(username=args["username"], password_hash=password)
            # users = db.session.query(User).all()
            data = db.session.query(User).filter_by(username=args["username"]).first()
            if data:
                return {"message":"user already exists"}, 403
            else:
                db.session.add(user)
                db.session.commit()
                return {"message": "success"}
        except:
            return {"message": "signup failed"}, 403


    def get(self):
        logger.debug("Inisde the get method of Task")
        return {"message" : "Inside get method"},200

    def put(self):
        logger.debug("Inisde the put method of Task")
        return {"message" : "Inside put method"},200

    def delete(sef):

        logger.debug("Inisde the delete method of Task")
        return {"message" : "Inside delete method"},200

class MerchantSignup(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',
                                 type=str,
                                 required=True,
                                 help='No name provided',
                                 location='json')
        self.parser.add_argument('password_hash',
                                 type=str,
                                 default="",
                                 location='json')
    # user_fields = {
    #     'id': fields.Integer,
    #     'username': fields.String,
    #     'password_hash': fields.String
    # }

    # @marshal_with(user_fields)
    def post(self):
        logger.debug("Inside the post method of Task")
        args = self.parser.parse_args()
        print(args)
        try:
            password = hashlib.sha256((args["password_hash"]).encode())
            password = password.hexdigest()
            print("what is the password - ", password)
            user =  Merchant(username=args["username"], password_hash=password)
            # users = db.session.query(User).all()
            data = db.session.query(Merchant).filter_by(username=args["username"]).first()
            if data:
                return {"message":"user already exists"}, 403
            else:
                db.session.add(user)
                db.session.commit()
                return  {"message":"Merchant signup successful"}, 200
        except:
            return {"message": "signup failed"}, 403


    def get(self):
        logger.debug("Inisde the get method of Task")
        return {"message" : "Inside get method"},200

    def put(self):
        logger.debug("Inisde the put method of Task")
        return {"message" : "Inside put method"},200

    def delete(sef):

        logger.debug("Inisde the delete method of Task")
        return {"message" : "Inside delete method"},200


class AuthLogin(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',
                                 type=str,
                                 required=True,
                                 help='No name provided',
                                 location='json')
        self.parser.add_argument('password_hash',
                                 type=str,
                                 default="",
                                 location='json')
    user_fields = {
        'id': fields.Integer,
        'username': fields.String,
        'password_hash': fields.String
    }

    @marshal_with(user_fields)
    def post(self):
        logger.debug("Inside the post method of Task")
        args = self.parser.parse_args()
        print(args)
        try:
            # user = User(username=args["username"], password_hash=args["password_hash"])
            # users = db.session.query(User).all()
            password = hashlib.sha256((args["password_hash"]).encode())
            password = password.hexdigest()
            print("what is the password - ", password)
            data = db.session.query(User).filter_by(username=args["username"], password_hash=password).first()
                
            if data is not None:
                return data, 200
            else:
                return {"message": "wrong credentials"}, 403
        except:
            # data = db.session.query(User).filter_by(username=args["username"]).first()
            return {"message": "something went wrong"}, 500

    def get(self):
        logger.debug("Inisde the get method of Task")
        return {"message" : "Inside get method"},200

    def put(self):
        logger.debug("Inisde the put method of Task")
        return {"message" : "Inside put method"},200

    def delete(sef):

        logger.debug("Inisde the delete method of Task")
        return {"message" : "Inside delete method"},200


class MerchantLogin(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',
                                 type=str,
                                 required=True,
                                 help='No name provided',
                                 location='json')
        self.parser.add_argument('password_hash',
                                 type=str,
                                 default="",
                                 location='json')
    user_fields = {
        'id': fields.Integer,
        'username': fields.String,
        'password_hash': fields.String
    }

    @marshal_with(user_fields)
    def post(self):
        logger.debug("Inside the post method of Task")
        args = self.parser.parse_args()
        print(args)
        try:
            # user = User(username=args["username"], password_hash=args["password_hash"])
            # users = db.session.query(User).all()
            password = hashlib.sha256((args["password_hash"]).encode())
            password = password.hexdigest()
            print("what is the password - ", password)
            data = db.session.query(Merchant).filter_by(username=args["username"], password_hash=password).first()
                
            if data is not None:
                return data, 200
            else:
                return {"message": "wrong credentials"}, 403
        except:
            # data = db.session.query(User).filter_by(username=args["username"]).first()
            return {"message": "something went wrong"}, 500

    def get(self):
        logger.debug("Inisde the get method of Task")
        return {"message" : "Inside get method"},200

    def put(self):
        logger.debug("Inisde the put method of Task")
        return {"message" : "Inside put method"},200

    def delete(sef):

        logger.debug("Inisde the delete method of Task")
        return {"message" : "Inside delete method"},200


