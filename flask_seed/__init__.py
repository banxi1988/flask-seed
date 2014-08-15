#-*- coding:utf-8 -*-
import os
import os.path
import logging
from flask import Flask

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '@|3*0)ae%w'
WWW_DIR = os.path.join(os.path.abspath(app.root_path+'/../'),'www')
logger.info('WWW_DIR'+WWW_DIR)

if not os.path.isdir(WWW_DIR):
    os.mkdir(WWW_DIR)
UPLOAD_FOLDER = os.path.join(WWW_DIR,'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
_img_dir = os.path.join(UPLOAD_FOLDER,'imgs')
if not os.path.isdir(_img_dir):
    os.mkdir(_img_dir)
app.config['IMG_UPLOAD_FOLDER'] = _img_dir
_questions_dir = os.path.join(UPLOAD_FOLDER,'questions')
if not os.path.isdir(_questions_dir):
    os.mkdir(_questions_dir)
app.config['QUESTIONS_UPLOAD_FOLDER'] = _questions_dir
app.config['MAX_CONTENT_LENGTH'] = 1*1024*1024 # max upload file size i 1M

import flask_seed.plugins
import flask_seed.views

