from app import db
import os
import time
from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer
from datetime import datetime

class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    created_at = db.Column(db.String, default=datetime.now()) ##db.Column(db.DateTime(timezone=True), default=func.now())
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'),nullable=False)
    items = db.relationship('Item', backref='shop', lazy=True) ## this is one to many relationaship, here we access other details as shop.items, just pass shop_is as foreign key in item id, which will be hidden in frontend
    pincode = db.Column(db.String(15))
    mobile = db.Column(db.String(15))
    location = db.Column(db.String(300))
    opening_time = db.Column(db.String) ##db.Column(db.DateTime(timezone=True), default=func.now())
    closing_time = db.Column(db.String)
    description = db.Column(db.String)
    home_delivery_available = db.Column(db.Boolean)
    is_deleted = db.Column(db.Boolean)


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
