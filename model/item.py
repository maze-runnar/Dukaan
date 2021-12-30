from app import db
from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    is_available = db.Column(db.Boolean, default=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'),nullable=False)
    max_order_amount = db.Column(db.String(20))
    min_order_amount = db.Column(db.String(20))
    imageUrl = db.Column(db.String(500))
    description = db.Column(db.String(500))
    is_deleted = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(50), default="other")


    def __init__(self, name, is_available, shop_id, max_order_amount, min_order_amount, description, imageUrl,category):
        self.name = name
        self.is_available = is_available
        self.shop_id = shop_id
        self.max_order_amount = max_order_amount
        self.min_order_amount = min_order_amount
        self.description = description
        self.imageUrl = imageUrl
        self.category = category
        db.create_all()
