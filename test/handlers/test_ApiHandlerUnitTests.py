#!/usr/bin/python2.7
""" ApiHandler Class Unit Tests. These use cases provide code coverage for
    the ApiHandler class. These unit tests test how the inputs are broken
    down, and put back together to return to the end user.

"""

__name__ = 'ApidHandlerUnitTests'

import unittest

import tornado.web
import tornado.ioloop
import tornado.testing
import tornado.httpserver

from valapi.handlers.ApiHandler import ApiHandler


class ApiHandlerUnitTests(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        self.app = tornado.web.Application([('/api/', ApiHandler)])
        self.maxDiff = None
        return self.app

    def test_api_all_success(self):
        '''Tests that best case scenario is handled as expected.'''
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

        data_input = {
            "first_name": "John",
            "last_name": "Smith",
            "dob": "01/12/1972",
            "address": "333 W 35th St, Chicago, IL",
            "zip_code": "60616",
            "phone_number": "1(310)456-1234",
            "account_number": 42942315
        }
        encoded_data_input = tornado.escape.json_encode(data_input)
        headers = {"Content-Type": "application/json"}

        response = self.fetch('/api/', method='POST', headers=headers,
                              body=encoded_data_input)

        json_body = tornado.escape.json_decode(response.body)
        self.assertDictEqual(expected_result, json_body)

    def test_api_all_fields_fail(self):
        '''Tests that worst case scenario is handled as expected.'''
        expected_result = {
            "status": "failed",
            "fields": {
                "first_name": "missing required field",
                "last_name": "missing required field",
                "dob": "person too young",
                "zip_code": "invalid format",
                "phone_number": "invalid format",
                "account_number": "invalid account number"
            },
            "data": {
                "first_name": "",
                "last_name": "",
                "dob": "01/12/2015",
                "address": "333 W 35th St, Chicago, IL",
                "zip_code": "60",
                "phone_number": "1234",
                "account_number": 4
            }
        }

        data_input = {
            "first_name": "",
            "last_name": "",
            "dob": "01/12/2015",
            "address": "333 W 35th St, Chicago, IL",
            "zip_code": "60",
            "phone_number": "1234",
            "account_number": 4
        }
        encoded_data_input = tornado.escape.json_encode(data_input)
        headers = {"Content-Type": "application/json"}

        response = self.fetch('/api/', method='POST', headers=headers,
                              body=encoded_data_input)

        json_body = tornado.escape.json_decode(response.body)
        self.assertEqual(response.code, 400)
        self.assertDictEqual(expected_result, json_body)

    def test_api_whitespaces_in_input(self):
        '''Tests that white spaces still return valid.'''
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

        data_input = {
            "first_name": " John ",
            "last_name": " Smith ",
            "dob": " 01/12/1972 ",
            "address": " 333 W 35th St, Chicago, IL ",
            "zip_code": " 60616 ",
            "phone_number": "1(310)456-1234",
            "account_number": 42942315
        }
        encoded_data_input = tornado.escape.json_encode(data_input)
        headers = {"Content-Type": "application/json"}

        response = self.fetch('/api/', method='POST', headers=headers,
                              body=encoded_data_input)

        json_body = tornado.escape.json_decode(response.body)
        self.assertDictEqual(expected_result, json_body)


if __name__ == '__main__':
    unittest.main()
