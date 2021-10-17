from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
from model.notification import Notification
from app import db

class NotificationPost(Resource):
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('msg',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_read',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('user_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('created_at',
                                     type=str,
                                     location='json')
        
    

    def post(self):
        logger.debug("Inside the post method of Notification")
        args = self.parser.parse_args()
        print("args coming ...",args)
        # print(name)
        item = Notification(msg=args["msg"], is_read=args["is_read"], created_at=args["created_at"],merchant_id=args["merchant_id"],user_id=args["user_id"])
        # item.name = args["name"]
        # item.merchant_id = args["merchant_id"]
        db.session.add(item)
        db.session.commit()
        return {"msg":args["msg"], "is_read":args["is_read"], "merchant_id":args["merchant_id"]}





class NotificationDetail(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('msg',
                                 type=str,
                                 location='json')
        self.parser.add_argument('is_read',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('user_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('created_at',
                                     type=str,
                                     location='json')
        

    
    def get(self, merchantid):
        logger.debug("Inisde the get method of Notification")
        data = db.session.query(Notification).filter_by(merchant_id=merchantid).all()
        
        notifications = []
        for i in data:
            x = {
                    "msg":i.msg,
                    "is_read":i.is_read,
                    "merchant_id":i.merchant_id,
                    "created_at":i.created_at
                }
    
            notifications.append(x)

        return {"data": notifications}

        

    def put(self, merchantid):
        logger.debug("Inisde the put method of Task")
        args = self.parser.parse_args()
        data = db.session.query(Notification).filter_by(merchant_id=merchantid).all()
        
        for i in data:
            i.is_read = True
            db.session.commit()
        return {"data": str(data)}, 200


    def delete(sef, notificationid):
        logger.debug("Inisde the delete method of Notification")   
        return {"message" : "user deleted"},200

