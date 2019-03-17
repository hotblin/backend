from flask import Flask
from .models import db


def register_blueprint(app):
    from .api import api
    app.register_blueprint(api)


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")
    register_blueprint(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
