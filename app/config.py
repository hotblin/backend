DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:123456@localhost:3306/sdzk_platform"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 安全配置
CSRF_ENABLED = True
SECRET_KEY = "hello"
