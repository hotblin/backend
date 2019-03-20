DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:123456@localhost:3306/sdzk_platform"
SQLALCHEMY_ECHO = False

# 安全配置
CSRF_ENABLED = True
SECRET_KEY = "hello"
