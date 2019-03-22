from flask import Flask
from .models import init_db
from flask_httpauth import HTTPTokenAuth
from flask_cors import CORS
from .views import register_blueprint

auth = HTTPTokenAuth(scheme='Bearer')
app = Flask(__name__)


def create_app():
    CORS(app, supports_credentials=True)
    app.config.from_object("app.config")
    register_blueprint(app)
    init_db(app)
    # with app.app_context():
    #     #     db.init_app(app)
    #     #     db.create_all()

    return app
