def register_blueprint(app):
    from .api import api
    app.register_blueprint(api)
