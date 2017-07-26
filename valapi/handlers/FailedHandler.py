#!/usr/bin/python2.7
""" This class describes how the failed handler sample data is returned to the
    end user.

"""

__name__ = 'FailedHandler'

import tornado.web


class FailedHandler(tornado.web.RequestHandler):

    def get(self):
        data = {
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

        response = tornado.escape.json_encode(data)
        self.set_status(400)
        self.write(response)
