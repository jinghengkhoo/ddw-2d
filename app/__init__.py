import os

from flask import Flask
from flask_bootstrap import Bootstrap5

from app.middleware import PrefixMiddleware

application = Flask(__name__)
bootstrap = Bootstrap5(application)
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)

SECRET_KEY = os.urandom(32)
application.config['SECRET_KEY'] = SECRET_KEY

from app import routes
