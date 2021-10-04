from flask import Flask
import logging as logger
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from marshmallow_sqlalchemy import *
# from flask_marshmallow import *


logger.basicConfig(level="DEBUG")


flaskAppInstance = Flask(__name__)

flaskAppInstance.config.from_object(Config)
db = SQLAlchemy(flaskAppInstance)
migrate = Migrate(flaskAppInstance, db)
# ma = Marshmallow(flaskAppInstance)
db.create_all()

if __name__ == '__main__':

    logger.debug("Starting Flask Server")
    from api import *
    flaskAppInstance.run(host="127.0.0.1",port=5000,debug=True,use_reloader=True)