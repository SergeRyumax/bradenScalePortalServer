#!/usr/bin/python
# coding=utf8

from flaskext.uploads import IMAGES

class LocalConfiguration(object):
	DATABASE = {
		'name': 'bradenscale',
		'host': 'localhost',
		'port': 3306,
		'user': 'root',
		'passwd': 'mysql',
		'engine': 'peewee.MySQLDatabase',
	}
	UPLOADS_DEFAULT_DEST='imagensupload/'
	UPLOADED_FILES_DEST='imagensupload/'
	UPLOADED_FILES_ALLOW=IMAGES