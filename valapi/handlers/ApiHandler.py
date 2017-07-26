#!/usr/bin/python2.7

__name__ = 'ApiHandler'

import tornado.web

from valapi.handlers.lib import Validator as val
#from handlers.lib import Validator as val

class ApiHandler(tornado.web.RequestHandler):

    def post(self):
        """Process the POST for a validation request."""

        response = {}
        failed_rules = {}
        processed_data = {}
        data = tornado.escape.json_decode(self.request.body)

        # get important data from HTTP request body
        if 'first_name' in data:
            first_name = data['first_name']
        else:
            first_name = ''

        first_name = data['first_name'] if 'first_name' in data else ''
        last_name = data['last_name'] if 'last_name' in data else ''
        dob = data['dob'] if 'dob' in data else ''
        address = data['address'] if 'address' in data else ''
        zip_code = data['zip_code'] if 'zip_code' in data else ''
        phone_number = data['phone_number'] if 'phone_number' in data else ''
        account_number = data['account_number'] if 'account_number' in data else ''

        # Validate inputs recieved
        (name_is_valid, message) = val.validate_name(first_name.strip())
        if name_is_valid:
            processed_data['first_name'] = message
        else:
            failed_rules['first_name'] = message
            processed_data['first_name'] = first_name

        (name_is_valid, message) = val.validate_name(last_name.strip())
        if name_is_valid:
            processed_data['last_name'] = message
        else:
            failed_rules['last_name'] = message
            processed_data['last_name'] = last_name

        (dob_is_valid, message) = val.validate_dob(dob.strip())
        if dob_is_valid:
            processed_data['dob'] = message
        else:
            failed_rules['dob'] = message
            processed_data['dob'] = dob

        (zip_code_is_valid, message) = val.validate_zip_code(zip_code.strip())
        if zip_code_is_valid:
            processed_data['zip_code'] = message
        else:
            failed_rules['zip_code'] = message
            processed_data['zip_code'] = zip_code

        (phone_number_is_valid, message) = val.validate_phone_number(phone_number.strip())
        if phone_number_is_valid:
            processed_data['phone_number'] = message
        else:
            failed_rules['phone_number'] = message
            processed_data['phone_number'] = phone_number

        (account_number_is_valid, message) = val.validate_account_number(account_number)
        if account_number_is_valid:
            processed_data['account_number'] = message
        else:
            failed_rules['account_number'] = message
            processed_data['account_number'] = account_number

        processed_data['address'] = address.strip()

        # inlcude processed data to the response
        response['data'] = processed_data

        if failed_rules:
            response['status'] = 'failed'
            response['fields'] = failed_rules
            self.set_status(400)
        else:
            response['status'] = 'valid'

        # publish reponse to the client
        self.set_header("Content-Type", "application/json")
        self.write(tornado.escape.json_encode(response))
