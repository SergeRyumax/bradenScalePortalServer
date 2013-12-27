#!/usr/bin/python
# coding=utf8
class LocalConfiguration(object):
	DATABASE = {
		'name': 'bradenscale',
		'host': 'localhost',
		'port': 3306,
		'user': 'root',
		'passwd': 'mysql',
		'engine': 'peewee.MySQLDatabase',
	}