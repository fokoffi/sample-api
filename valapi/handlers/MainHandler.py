#!/usr/bin/python2.7

__name__ = 'MainHandler'

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("welcome to the API.")
