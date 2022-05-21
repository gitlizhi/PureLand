#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import create_app
app = create_app()
print(app.url_map)

if __name__ == '__main__':
    app.run()

