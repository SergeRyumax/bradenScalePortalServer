import logging
from bradenscale import *

if(__name__) == '__main__':
	handler = logging.FileHandler('bradenscaleserver.log')
	handler.setLevel(logging.DEBUG)
	app.logger.addHandler(handler)
	app.run(debug=True)
