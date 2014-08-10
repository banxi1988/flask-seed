#-*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '@|3*0)ae%w'

import flask_seed.plugins
import flask_seed.views

