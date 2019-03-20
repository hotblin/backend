from flask import Flask
from .models import db
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

auth = HTTPBasicAuth()
app = Flask(__name__)


def register_blueprint(app):
    from .api import api
    app.register_blueprint(api)


def create_app():
    CORS(app)
    app.config.from_object("app.config")
    register_blueprint(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app
