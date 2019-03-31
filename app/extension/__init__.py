from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


# 统一初始化第三方框架


def init_extension(app):
    db.init(app)
    migrate.init_app(app, db)
