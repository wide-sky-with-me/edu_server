from app import db

# 判断题


class Tfq(db.Model):
    __tablename__ = 'tfq'
    # 自身的索引id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 题目内容
    content = db.Column(db.Text, nullable=False)

    # 问题编号
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    # 答案
    answer = db.Column(db.Enum(True, False), nullable=False)

    def __repr__(self):
        return f'<Tfq {self.id}>'
