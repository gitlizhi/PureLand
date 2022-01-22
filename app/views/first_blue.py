#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint
first_bp = Blueprint('first_bp', __name__)


@first_bp.route('/index', methods=['GET'])
def index():

    return "welcome to Pure Land"
    # return "your address is {}".format(request.remote_addr)
