#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()

