from bradenscale import app
#!/usr/bin/python
# coding=utf8
#assim ate eu usar um log decente
def e(e):
	app.logger.error(e)
	#print e
def i(i):
	app.logger.info(i)
	#print i
def d(d):
	app.logger.debug(d)
	#print d