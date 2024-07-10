from sqlalchemy import Nullable, null
from app import db


class Knowledge(db.Model):
    __tablename__ = 'knowledge'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, Nullable=False)

    questions = db.relationship(
        'Question', backref='knowledge', lazy='dynamic')

    def __repr__(self):
        return f'<Knowledge {self.id}>'

    @property
    def ocq_num(self):
        return len(self.questions.filter_by(type='ocq').all())

    @property
    def mcq_num(self):
        return len(self.questions.filter_by(type='mcq').all())

    @property
    def tfq_num(self):
        return len(self.questions.filter_by(type='tfq').all())

    @property
    def fbq_num(self):
        return len(self.questions.filter_by(type='fbq').all())

    @property
    def saq_num(self):
        return len(self.questions.filter_by(type='saq').all())
