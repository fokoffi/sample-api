#!/usr/bin/python2.7
""" FailedHandler Class Unit Tests

"""

__name__ = 'FailedHandlerUnitTests'

import unittest

import tornado.web
import tornado.ioloop
import tornado.testing
import tornado.httpserver

from valapi.handlers.FailedHandler import FailedHandler


class FailedHandlerUnitTests(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        self.app = tornado.web.Application([('/failed/', FailedHandler)])
        self.maxDiff = None
        return self.app

    def test_expected_failed_output_is_returned(self):
        expected_result = {
            "status": "failed",
            "fields": {
                "first_name": "missing required field"
            },
            "data": {
                "first_name": "",
                "last_name": "McIntyre",
                "dob": "11/22/1982",
                "address": "One E161st St,Bronx,NY",
                "zip_code": "10451",
                "phone_number": "(310) 654-3412",
                "account_number": 42942315
            }
        }
        headers = {"Content-Type": "application/json"}

        response = self.fetch('/failed/', method='GET', headers=headers)
        body = tornado.escape.json_decode(response.body)

        self.assertEqual(response.code, 400)
        self.assertDictEqual(expected_result, body)


if __name__ == '__main__':
    unittest.main()
