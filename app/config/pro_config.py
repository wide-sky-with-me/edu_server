from .base_config import BaseConfig


class ProConfig(BaseConfig):
    # Debug
    DEBUG = False
    # 数据库配置
    MYSQL_HOST = 'xxxx'
    MYSQL_PORT = 3306
    MYSQL_USER = 'xxxx'
    MYSQL_PASSWORD = 'xxxx'
    MYSQL_DB = 'xxxx'
    MYSQL_CHARSET = 'utf8mb4'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{
        MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
