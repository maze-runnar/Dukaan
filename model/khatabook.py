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

class Khata(db.Model):
    __tablename__ = 'khata'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    payer_name = db.Column(String)
    mark_as_paid = db.Column(db.Boolean, default=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'),nullable=False)
    merchant_id = db.Column(db.Integer)
    total_money = db.Column(db.Integer)
    paid_money = db.Column(db.Integer)
    description = db.Column(db.String)
    created_at = db.Column(db.String, default=datetime.now())



    def __init__(self, title, mark_as_paid, shop_id, merchant_id, total_money, paid_money, description, created_at, payer_name):
        self.title = title
        self.mark_as_paid = mark_as_paid
        self.shop_id = shop_id
        self.merchant_id = merchant_id
        self.total_money = total_money
        self.paid_money = paid_money
        self.description = description
        self.created_at = created_at
        self.payer_name = payer_name
        db.create_all()
