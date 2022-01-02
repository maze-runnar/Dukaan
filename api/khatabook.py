from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
from model.khatabook import Khata
from app import db

class KhataPost(Resource):
    def __init__(self):
        """Parse arguments from json"""

        
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',
                                 type=str,
                                 location='json')
        self.parser.add_argument('mark_as_paid',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('shop_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('total_money',
                                 type=int,
                                 location='json')
        self.parser.add_argument('paid_money',
                                 type=int,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('created_at',
                                 type=str,
                                 location='json')
        self.parser.add_argument('payer_name',
                                 type=str,
                                 location='json')

    def post(self):
        logger.debug("Inside the post method of Task")
        args = self.parser.parse_args()
        print("args coming ...",args)
        # print(name)
        record = Khata(title=args["title"], mark_as_paid=args["mark_as_paid"], shop_id=args["shop_id"],merchant_id=args["merchant_id"], total_money=args["total_money"], paid_money=args["paid_money"], description=args['description'], created_at=args["created_at"], payer_name=args["payer_name"])
        db.session.add(record)
        db.session.commit()
        return {"title":args["title"], "mark_as_paid":args["mark_as_paid"], "shop_id":args["shop_id"], "merchant_id": args["merchant_id"], "total_money": args["total_money"], "paid_money": args["paid_money"], "created_at": args["created_at"], "payer_name": args["payer_name"]}





class KhataDetail(Resource):

    
    def __init__(self):
        """Parse arguments from json"""


        
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',
                                 type=str,
                                 location='json')
        self.parser.add_argument('mark_as_paid',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('shop_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('total_money',
                                 type=int,
                                 location='json')
        self.parser.add_argument('paid_money',
                                 type=int,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('created_at',
                                 type=str,
                                 location='json')
        self.parser.add_argument('payer_name',
                                 type=str,
                                 location='json')
            
    

    
    def get(self, khataid):
        logger.debug("Inisde the get method of Task")
        data = Khata.query.get(khataid)
        # res = jsonify(data)
        # print("here is the response", make_response(jsonify(data)))
        return {
                    "data" : {"title": data.title,"payer_name": data.payer_name,"mark_as_paid": data.mark_as_paid, "shop_id": data.shop_id, "merchant_id": data.merchant_id, "total_money": data.total_money, "paid_money": data.paid_money, "created_at": data.created_at}
                }

    def put(self, khataid):
        logger.debug("Inisde the put method of Task")
        args = self.parser.parse_args()
        # print("args coming ...",args)
        data = Khata.query.get(khataid)
        data.mark_as_paid = args["mark_as_paid"]
        data.total_money = args["total_money"]
        data.paid_money = args["paid_money"]
        db.session.commit()
        return {"data": str(data)},200

    def delete(sef, itemid):

        logger.debug("Inisde the delete method of Task")   
        return {"message" : "user deleted"},200



class KhataList(Resource):

    
    def __init__(self):
        """Parse arguments from json"""

        
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',
                                 type=str,
                                 location='json')
        self.parser.add_argument('mark_as_paid',
                                 type=bool,
                                 location='json')
        self.parser.add_argument('shop_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('merchant_id',
                                 type=int,
                                 location='json')
        self.parser.add_argument('total_money',
                                 type=int,
                                 location='json')
        self.parser.add_argument('paid_money',
                                 type=int,
                                 location='json')
        self.parser.add_argument('description',
                                 type=str,
                                 location='json')
        self.parser.add_argument('created_at',
                                 type=str,
                                 location='json')
        self.parser.add_argument('payer_name',
                                 type=str,
                                 location='json')
        
        
    def get(self, shopid):
        logger.debug("Inisde the get method of Task")
        data = db.session.query(Khata).filter_by(shop_id=shopid).all()
        
        records = []
        for i in data:
            x = {
                    "title":i.title,
                    "mark_as_paid":i.mark_as_paid,
                    "shop_id":i.shop_id,
                    "merchant_id": i.merchant_id,
                    "description": i.description,
                    "paid_money": i.paid_money,
                    "total_money": i.total_money,
                    "payer_name": i.payer_name
                }
    
            records.append(x)

        return {"data": records}
