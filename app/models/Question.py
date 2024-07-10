from enum import auto
from flask_sqlalchemy import SQLAlchemy
from app import db
from .Type import Type
from .Difficulty import Difficulty


class Question():
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Enum(Type), nullable=False)
    difficulty = db.Column(db.Enum(Difficulty), nullable=False)
