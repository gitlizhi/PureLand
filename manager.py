#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app
app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)
print(app.url_map)

if __name__ == '__main__':
    manager.run()

