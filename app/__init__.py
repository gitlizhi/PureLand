#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, make_response, render_template
from flask_migrate import Migrate
from app.ext import db
from app.views import init_views
from app.users import *
from config import basedir

migrate = Migrate()


def create_app():
    app = Flask(__name__, static_folder='', static_url_path='', template_folder=basedir + '/templates')
    # app.config.from_object(config['production'])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@127.0.0.1:3306/pureland'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # init_ext(app)
    init_views(app)
    init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    return app


def init_app(app):
    @app.errorhandler(404)
    def get_404(e):
        return make_response(render_template('404.html'), 404)
