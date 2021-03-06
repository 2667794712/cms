from exts import db
from datetime import datetime


class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)  # 不能为空
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)  # 不能重复
    join_time = db.Column(db.DateTime, default=datetime.now)
