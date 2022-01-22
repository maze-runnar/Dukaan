from app import db
import os
import time
from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer
from datetime import datetime

class ShopImages(db.Model):
    __tablename__ = "shopimages"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    url = db.Column(db.String)
    shop_id = db.Column(db.Integer, db.ForeignKey(
        'shops.id'), nullable=False)

    def __init__(self, title, url, shop_id):
        self.title = title
        self.url = url
        self.shop_id = shop_id
        db.create_all()
        

class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    # db.Column(db.DateTime(timezone=True), default=func.now())
    created_at = db.Column(db.String, default=datetime.now())
    merchant_id = db.Column(db.Integer, db.ForeignKey(
        'merchants.id'), nullable=False)
    # this is one to many relationaship, here we access other details as shop.items, just pass shop_is as foreign key in item id, which will be hidden in frontend
    items = db.relationship('Item', backref='shop', lazy=True)
    pincode = db.Column(db.String(15))
    mobile = db.Column(db.String(15))
    location = db.Column(db.String(300))
    # db.Column(db.DateTime(timezone=True), default=func.now())
    opening_time = db.Column(db.String)
    closing_time = db.Column(db.String)
    description = db.Column(db.String)
    home_delivery_available = db.Column(db.Boolean)
    is_deleted = db.Column(db.Boolean)
    images = db.relationship('ShopImages', backref='shopimage', lazy=True)


    def __init__(self, name, merchant_id, pincode, mobile, location, opening_time, closing_time, description, home_delivery_available, created_at):
        self.name = name
        self.merchant_id = merchant_id
        self.pincode = pincode
        self.mobile = mobile
        self.location = location
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.description = description
        self.created_at = created_at
        self.home_delivery_available = home_delivery_available
        db.create_all()
