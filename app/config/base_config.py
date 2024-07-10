

from pathlib import Path


class BaseConfig(object):
    # Debug
    DEBUG = False
    # testing
    TESTING = False

    # 运行域名和端口
    FLASK_RUN_HOST = '127.0.0.1'
    FLASK_RUN_PORT = 5001

    # 智谱清言api key
    ZHIPU_API_KEY = '508e735792a807ab9a8119eb524952c9.yNbfx40VvoQFEPbt'

    # 项目根目录
    BASE_DIR = Path(__file__).parent.parent.parent

    @staticmethod
    def init_app(app):
        pass
