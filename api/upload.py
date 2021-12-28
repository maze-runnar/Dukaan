from flask_restful import Resource, Api, reqparse, fields, marshal_with
import logging as logger
from flask import Flask, abort, request, jsonify, g, url_for, make_response
from model.item import Item
from app import db
import os
from werkzeug.utils import secure_filename
from uuid import uuid4


class ImageUpload(Resource):
    def __init__(self):
        """Parse arguments from json"""

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('file',
                                 type=str,
                                 location='json')
        

    def post(self):
        app_root = os.path.dirname(os.path.abspath(__file__))
        target = os.path.join(app_root, '../static/images/uploads')
        ret = ""
        if not os.path.isdir(target):
            os.makedirs(target)
        if "file" in request.files:
            file = request.files['file']
            if file is None:
                pass
            else:
                file_name = uuid4().__str__()[:8] + secure_filename(file.filename) or ''
                destination = '/'.join([target, file_name])
                file.save(destination)
                ret = url_for('static',filename = 'images/uploads/' + file_name)
        else:
            ret = "please upload any file"
        # session['uploadFilePath']=destination
        return {"data": ret}
        