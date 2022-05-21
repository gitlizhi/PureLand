#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, url_for, redirect
first_bp = Blueprint('first_bp', __name__)


@first_bp.route('/index', methods=['GET'])
def index():

    return "welcome to Pure Land"
    # return "your address is {}".format(request.remote_addr)


@first_bp.route('/', methods=['GET'])
def index_302():
    # 重定向
    # return redirect(url_for('first_bp.index'))
    return redirect('/index')