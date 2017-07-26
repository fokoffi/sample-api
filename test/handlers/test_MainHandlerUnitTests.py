#!/usr/bin/python2.7
""" MainHandler Class Unit Tests

"""

__name__ = 'MainHandlerUnitTests'

import unittest

import tornado.web
import tornado.ioloop
import tornado.testing
import tornado.httpserver

from valapi.handlers.MainHandler import MainHandler


class MainHandlerUnitTests(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        self.app = tornado.web.Application([('/', MainHandler)])
        return self.app

    def test_endpoint_works(self):
        headers = {"Content-Type": "application/json"}

        response = self.fetch('/', method='GET', headers=headers)
        self.assertEqual(response.code, 200)
        self.assertEqual('welcome to the API.', response.body)


if __name__ == '__main__':
    unittest.main()
