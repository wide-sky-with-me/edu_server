from .base_config import BaseConfig


class DevConfig(BaseConfig):

    # Debug
    DEBUG = True
    # 数据库配置
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'qaz398277'
    MYSQL_DB = 'question_database'
    MYSQL_CHARSET = 'utf8mb4'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{
        MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
