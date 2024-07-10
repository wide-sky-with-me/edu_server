from app import db


# 简答题
class Saq(db.Model):
    __tablename__ = 'saq'
    # 自身的索引id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 题目内容
    content = db.Column(db.Text, nullable=False)

    # 问题编号
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    # 答案
    answer = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Saq {self.id}>'
