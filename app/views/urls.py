#!/usr/bin/python
# -*- coding: utf-8 -*-
from .user import get_user_bp_obj, UserReource


user_url_route = [
    (UserReource, '/ab'),
]


def get_user_bp(url_route, url_prefix=None):
    return get_user_bp_obj('user_bp', *url_route, url_prefix=url_prefix)


user_bp = get_user_bp(user_url_route, url_prefix='/user')



