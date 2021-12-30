from app import db
import os
import time
from flask import Flask, abort, request, jsonify, g, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer
from datetime import datetime

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(1000))
    is_read = db.Column(db.Boolean)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'),nullable=False)
    uesr_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    created_at = db.Column(db.String, default=datetime.now()) ##db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, msg, is_read, created_at, merchant_id, user_id):
        self.msg = msg
        self.is_read = is_read
        self.created_at = created_at
        self.merchant_id = merchant_id
        self.uesr_id = user_id
        db.create_all()
