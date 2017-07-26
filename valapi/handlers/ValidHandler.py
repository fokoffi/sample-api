#!/usr/bin/python2.7
""" This class describes how the valid handler sample data is returned to the
    end user.

"""

__name__ = 'ValidHandler'

import tornado.web


class ValidHandler(tornado.web.RequestHandler):

    def get(self):
        data = {
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

        response = tornado.escape.json_encode(data)
        self.write(response)
