#!/usr/bin/python
# -*- coding: utf-8 -*-
from app.ext import db


class User(db.Model):
    __tablename__ = 't_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.SmallInteger)
    gender = db.Column(db.Enum("1", "2"))  # 1, man  2, woman
    addr = db.Column(db.String(256))
    mobile = db.Column(db.String(11))
    create_time = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        self.commit()

    @classmethod
    def commit(cls):
        db.session.commit()



