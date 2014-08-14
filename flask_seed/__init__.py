#-*- coding:utf-8 -*-
import os.path
import logging
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '@|3*0)ae%w'
UPLOAD_FOLDER = os.path.expanduser('~/Tmp/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['IMG_UPLOAD_FOLDER'] = os.path.join(UPLOAD_FOLDER,'imgs')
app.config['QUESTIONS_UPLOAD_FOLDER'] = os.path.join(UPLOAD_FOLDER,'questions')
app.config['MAX_CONTENT_LENGTH'] = 1*1024*1024 # max upload file size i 1M
logging.basicConfig(level=logging.DEBUG)

import flask_seed.plugins
import flask_seed.views

