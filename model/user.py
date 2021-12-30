from app import db
import os
import time
from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer
from model.item import Item



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    name = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    location = db.Column(db.String(300))
    pincode = db.Column(db.String(15))
    bucket = db.Column(db.String(1000))
    personal_note = db.Column(db.String(2000))
    favourites = db.Column(db.String(1000))
    is_verified = db.Column(db.Boolean)
    mobile = db.Column(db.String(15))


    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        db.create_all()

class Merchant(db.Model):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    name = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    location = db.Column(db.String(300))
    authy_user_id = db.Column(db.String(30))
    pincode = db.Column(db.String(15))
    personal_note = db.Column(db.String(2000))
    is_verified = db.Column(db.Boolean)
    mobile = db.Column(db.String(15))

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        db.create_all()

