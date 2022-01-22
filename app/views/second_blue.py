#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint
second_bp = Blueprint('second_bp', __name__)


@second_bp.route('/sec', methods=['GET'])
def sec():
    return "这是第2个蓝图"
