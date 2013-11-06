#!/usr/bin/python
# coding=utf8
from flask import Flask
from flask_peewee.db import Database
from flaskext.uploads import *

app = Flask(__name__)

import log

app.config.from_object('config.LocalConfiguration')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

app.config['DEBUG'] = True
log.i('Configuração de Banco de Dados:'+str(app.config['DATABASE']))

db = Database(app)

from api import *