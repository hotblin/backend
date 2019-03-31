
def get_db_uri(db_info):
    ENGINE = db_info.get("ENGINE") or 'mysql'
    DRIVER = db_info.get("DRIVER") or 'cymysql'
    USER = db_info.get("USER") or 'root'
    PASSWORD = db_info.get("PASSWORD") or '123456'
    HOST = db_info.get("HOST") or 'localhost'
    PORT = db_info.get("PORT") or '3306'
    DBNAME = db_info.get("DBNAME") or 'sdzk_platform'
    # "mysql+cymysql://root:123456@localhost:3306/sdzk_platform"
    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, DBNAME)


class Config:
    DEBUG = False
    SECRET_KEY = "base_config"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # 安全配置
    CSRF_ENABLED = True


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "cymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "DBNAME": 'sdzk_platform'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    "develop":DevelopConfig
}