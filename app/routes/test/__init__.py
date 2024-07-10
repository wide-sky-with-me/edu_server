
from flask import Blueprint, Flask

test_bp = Blueprint('test', __name__)


def init_app(app: Flask):
    from . import service
    app.register_blueprint(test_bp, url_prefix='/test')
