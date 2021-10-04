from app import db
import os
import time
from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    is_available = db.Column(db.Boolean)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'),nullable=False)

    def __init__(self, name, is_available, merchant_id):
        self.name = name
        self.is_available = is_available
        self.merchant_id = merchant_id
        db.create_all()
