from app import db

# 填空题


class Fbq(db.Model):
    __tablename__ = 'fbq'
    # 自身的索引id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 题目内容
    content = db.Column(db.Text, nullable=False)

    # 问题编号
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    # 答案
    answer = db.Column(db.JSON, nullable=False)

    # 关联问题
    question = db.relationship(
        'Question', backref=db.backref('fbq', uselist=False))

    def __repr__(self):
        return f'<Fbq {self.id}>'
