from flask import Blueprint, Flask

generate_question = Blueprint('generate_question', __name__)


def init_app(app: Flask):
    from . import service
    app.register_blueprint(generate_question, url_prefix='/')
