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
        self.parser.add_argument('category',
                                 type=str,
                                 location='json')
        self.parser.add_argument('imageUrl',
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
        item = Item(name=args["name"], is_available=args["is_available"], shop_id=args["shop_id"],max_order_amount=args["max_order_amount"], min_order_amount=args["min_order_amount"], description=args["description"], category=args['category'], imageUrl=args["imageUrl"])
        db.session.add(item)
        db.session.commit()
        return {"name":args["name"], "is_available":args["is_available"], "shop_id":args["shop_id"], "category": args["category"]}





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
        self.parser.add_argument('category',
                                 type=str,
                                 location='json')
        self.parser.add_argument('imageUrl',
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
                                "min_order_amount": data.min_order_amount,
                                "category": data.category
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
        self.parser.add_argument('category',
                                 type=str,
                                 location='json')
        self.parser.add_argument('imageUrl',
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
                    "description": i.description,
                    "category": i.category
                }
    
            items.append(x)

        return {"data": items}

class ItemListByCategory(Resource):
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
                                 type=str,
                                 location='json')
        
    
    def get(self):
        category = request.args.get('category')
        limit = 50
        if request.args.get('limit'):
            limit = request.args.get('limit')


        data = Item.query.filter(Item.category.ilike(f'%{category}%')).limit(limit).all()
        items = []
        for i in data:
            items.append({
                "id": i.id,
                "name":i.name,
                "is_available":i.is_available,
                "shop_id":i.shop_id,
                "description": i.description,
                "max_order_amount": i.max_order_amount,
                "min_order_amount": i.min_order_amount,
                "category": i.category
            })
        return {
            "data": items
        }   


class ItemListByName(Resource):
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name',
                                 type=str,
                                 location='json')
        

    
    def get(self):
        itemname = request.args.get('itemname')
        limit = 50
        if request.args.get('limit'):
            limit = request.args.get('limit')


        data = Item.query.filter(Item.name.ilike(f'%{itemname}%')).limit(limit).all()
        items = []
        for i in data:
            items.append({
                "id": i.id,
                "name":i.name,
                "is_available":i.is_available,
                "shop_id":i.shop_id,
                "description": i.description,
                "max_order_amount": i.max_order_amount,
                "min_order_amount": i.min_order_amount,
                "category": i.category
            })
        return {
            "data": items
        }   
