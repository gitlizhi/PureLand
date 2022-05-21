#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from app.users import User
from datetime import datetime


def get_user_bp_obj(bp_name, *args, url_prefix=None):
    """
    获取蓝图对象
    :param bp_name: 蓝图名称
    :param args: 多组视图类和url路径的组合
    :param url_prefix: 蓝图统一路由前缀
    :return: 蓝图对象
    """
    user_bp = Blueprint(bp_name, __name__, url_prefix=url_prefix)
    api = Api(user_bp)
    for i in args:
        view_class, path = i[0], i[1]
        api.add_resource(view_class, path)
    return user_bp


class UserReource(Resource):
    """用户表,增删改查"""

    def __init__(self):
        self.rp = RequestParser()

    def get(self):
        self.rp.add_argument('id', required=True, type=int, location='args')
        new_rp = self.rp.parse_args()
        user = User.query.filter(User.id == new_rp.id).first()
        if user:
            return {"username": user.name, "age": user.age}
        else:
            return {"username": None}

    def post(self):
        self.rp.add_argument('name', type=str, location='json')
        self.rp.add_argument('age', type=int, location='json')
        self.rp.add_argument('gender', type=str, location='json')
        self.rp.add_argument('addr', default=None, location='json')
        self.rp.add_argument('mobile', location='json', default=None)

        new_rp = self.rp.parse_args()
        try:
            User(name=new_rp.name,
                 age=new_rp.age,
                 gender=new_rp.gender,
                 addr=new_rp.addr,
                 mobile=new_rp.mobile,
                 create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                 ).save()
        except:
            return '保存失败'
        return '保存成功'

    def put(self):
        self.rp.add_argument('id', type=int, location='json', required=True)
        self.rp.add_argument('name', type=str, location='json')
        self.rp.add_argument('age', type=int, location='json')
        self.rp.add_argument('gender', type=str, location='json')
        self.rp.add_argument('addr', default=None, location='json')
        self.rp.add_argument('mobile', location='json', default=None)

        new_rp = self.rp.parse_args()

        try:
            User.query.filter(User.id == new_rp.id).update({'name': new_rp.name,
                                                            'age': new_rp.age,
                                                            'gender': new_rp.gender,
                                                            'addr': new_rp.addr,
                                                            'mobile': new_rp.mobile
                                                            })
            User.commit()
            return '修改成功'
        except:
            return '修改失败'

    def delete(self):
        self.rp.add_argument('id', type=int, location='json', required=True)
        new_rp = self.rp.parse_args()
        if new_rp.id:
            User.query.filter(User.id == new_rp.id).delete()
            User.commit()
        return '删除成功'

