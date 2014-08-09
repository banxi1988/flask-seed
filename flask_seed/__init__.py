#-*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)

import flask_seed.plugins
import flask_seed.views

