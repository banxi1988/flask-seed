#-*- coding:utf-8 -*-
from flask import Response
from flask_seed import app
from .plugins import admin_permission

# protect a permission with a single Need, in this case a RoleNeed
@app.route('/admin')
@admin_permission.require()
def do_admin_index():
    return Response("Only if you are an admin")

# this time protect with a context mananger
@app.route('/articles')
def do_articles():
    with admin_permission.require():
        return Response('Only if you are admin')

