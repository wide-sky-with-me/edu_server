
from app import db


#单选题
class Ocq(db.Model):
    __tablename__ = 'ocq'
    # 自身的索引id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 题目内容
    content = db.Column(db.Text, nullable=False)

    # 问题编号
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    # 选项
    choices = db.Column(db.JSON, nullable=False)
    # 答案
    answer = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f'<Ocq {self.id}>'
