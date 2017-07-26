#!/usr/bin/python2.7
""" ValidHandler Class Unit Tests

"""

__name__ = 'ValidHandlerUnitTests'

import unittest

import tornado.web
import tornado.ioloop
import tornado.testing
import tornado.httpserver

from valapi.handlers.ValidHandler import ValidHandler


class ValidHandlerUnitTests(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        self.app = tornado.web.Application([('/valid/', ValidHandler)])
        self.maxDiff = None
        return self.app

    def test_valid_result_is_returned(self):
        expected_result = {
            "status": "valid",
            "data": {
                "first_name": "John",
                "last_name": "Smith",
                "dob": "01/12/1972",
                "address": "333 W 35th St, Chicago, IL",
                "zip_code": "60616",
                "phone_number": "(310) 456-1234",
                "account_number": 42942315
            }
        }
        headers = {"Content-Type": "application/json"}

        response = self.fetch('/valid/', method='GET', headers=headers)
        body = tornado.escape.json_decode(response.body)

        self.assertEqual(response.code, 200)
        self.assertDictEqual(expected_result, body)


if __name__ == '__main__':
    unittest.main()
