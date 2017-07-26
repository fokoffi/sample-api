#!/usr/bin/python2.7

import sys

import tornado.web
import tornado.ioloop
import tornado.httpserver

from valapi.handlers.ApiHandler import ApiHandler
from valapi.handlers.MainHandler import MainHandler
from valapi.handlers.ValidHandler import ValidHandler
from valapi.handlers.FailedHandler import FailedHandler


def main():
    app = tornado.web.Application([
        (r'/', MainHandler),

        # Sample valid and failed handlers
        (r'/valid/', ValidHandler),
        (r'/failed/', FailedHandler),

        # API Version 1.0
        (r'/api/', ApiHandler)
    ], debug=True, autoreload=True)

    server = tornado.httpserver.HTTPServer(app)

    # Single-process dev code:
    server.listen(2016)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
    sys.exit(0)
