#-*- coding:utf-8 -*-
import os.path
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '@|3*0)ae%w'
app.config['UPLOAD_FOLDER'] = os.path.expanduser('~/Tmp/uploads')
app.config['MAX_CONTENT_LENGTH'] = 1*1024*1024 # max upload file size i 1M

import flask_seed.plugins
import flask_seed.views

