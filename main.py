#!/usr/bin/env python
from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.api import memcache
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class HelloWorldHandler(webapp.RequestHandler):
	def get(self):

		# Collect an HTML Template
		path = os.path.join(os.path.dirname(__file__),'template.html')
		# Write the response
		self.response.out.write(template.render(path, {}))


application = webapp.WSGIApplication([
	('/', HelloWorldHandler)
	],debug=True)

def main():
	run_wsgi_app(application)

if __name__ == '__main__':
	main()