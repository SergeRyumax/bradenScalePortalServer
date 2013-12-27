#!/usr/bin/python
# coding=utf8
from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)

import log

app.config.from_object('config.LocalConfiguration')

app.config['DEBUG'] = True
log.i('Configuração de Banco de Dados:'+str(app.config['DATABASE']))

db = Database(app)

from api import *