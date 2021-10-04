import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'hope-is-a-dangerous-thing-to-lose'
#    SECRET_KEY = os.environ.get('SECRET_KEY') or 'do-or-do-not-there-is-no-try'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'paasme.db')
    SQLALCHEMY_DATABASE_URI = "postgresql://sundaramdubey:sundaram@localhost:5432/paasme"
    SQLALCHEMY_TRACK_MODIFICATIONS = False