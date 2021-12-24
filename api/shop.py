from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
from model.item import Item
from model.user import User, Merchant
from app import db



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
            near_shops = Merchant.query.filter_by(pincode=user_pincode).all()
        merchants = []
        for i in near_shops:
            x = {
                "id": i.id,
                "location": i.location,
                "mobile": i.mobile
            }
            merchants.append(x)

        # logger.debug("Merchants near me: ", merchants)
        
        return {"data": merchants}

