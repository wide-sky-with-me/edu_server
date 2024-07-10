from flask import Flask


def register_blueprints(app: Flask):
    from .test import init_app as test_init_app
    test_init_app(app)
    from .generate_question import init_app as generate_question_init_app
    generate_question_init_app(app)
