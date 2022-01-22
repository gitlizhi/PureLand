#!/usr/bin/python
# -*- coding: utf-8 -*-
from .first_blue import first_bp
from .second_blue import second_bp
from .urls import user_bp


def init_views(app):
    app.register_blueprint(first_bp)
    app.register_blueprint(second_bp)
    app.register_blueprint(user_bp)

