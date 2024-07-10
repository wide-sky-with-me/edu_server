from flask import Flask
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

from flask_cors import CORS

moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(config[config_name])

    # 初始化moment
    moment.init_app(app)
    # 初始化数据库
    db.init_app(app)
    with app.app_context():
        try:
            db.create_all()  # 创建所有表
            app.logger.info("Database connected successfully.")
        except Exception as e:
            app.logger.error("Failed to connect to database.", exc_info=e)
    # 注册蓝图
    from .routes import register_blueprints
    register_blueprints(app)

    return app
