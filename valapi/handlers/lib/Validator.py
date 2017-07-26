#!/usr/bin/python2.7
""" This package has a list of functions that's used to validate all the
    different fields that are to be evaluated before being returned to the
    end user.
"""
__name__ = 'Validator'

import re

from datetime import datetime


def validate_name(name):
    ''' Validate name passed in as param.

        Return a tuple of a boolean and a status message. The boolean returns
        True if the param is valid, False otherwise. The status message
        explains the issue when returning False.

    '''
    if not name:
        return False, 'missing required field'
    else:
        if name.isupper() or name.islower():
            name = name.title()
        return True, name


def validate_dob(dob):
    '''Assuming data is always in format: MM/DD/YYYY.

       Return True if person is < 110yo and > 17yo. Else, return a string
       with the description of the error. If False, return a status message.
       Return status message is empty string if True is returned.

    '''
    max_age = 110
    min_age = 18

    today = datetime.now()

    if '/' in dob:
        (month, day, year) = dob.split('/')
    elif '.' in dob:
        (month, day, year) = dob.split('.')
    elif '-' in dob:
        (month, day, year) = dob.split('-')

    # prepend '19' to year if it only contains two digits
    year = '19' + year if len(year) == 2 else year

    day = int(day)
    month = int(month)
    year = int(year)

    # TODO: Check if user is from another country where the month and day were
    # flipped.

    date_dob = datetime(year, month, day)
    age = round(((today - date_dob).days / 365.25), 0)

    if age > max_age:
        return False, 'person too old'
    elif age < min_age:
        return False, 'person too young'
    else:
        return True, date_dob.strftime("%m/%d/%Y")


def validate_zip_code(zip_code):
    ''' Validate that zip_code is either 5 or 9 digits.

        Return a tuple of a boolean and a status message. The boolean returns
        True if the param is valid, False otherwise. The status message
        explains the issue when returning False.

    '''
    re_zip_code = '(^\d{5}$)|(^\d{9}$)'
    zc = zip_code

    # remove commonly seen punctuation arround zip codes.
    for delim in (' - ', '-', ' '):
        zc = zc.replace(delim, '')

    if re.match(re_zip_code, zc):
        if len(zc) == 9:
            zc = zc[:5] + '-' + zc[5:]
        return True, zc
    else:
        return False, 'invalid format'


def validate_phone_number(phone_number):
    ''' Validate phone number is 10 digits. If it's 11 digits starting with a
        1, drop it off.

        Return a tuple of a boolean and a status message. The boolean returns
        True if the param is valid, False otherwise. The status message
        explains the issue when returning False.
    '''

    re_number = '(^\d{10}$)'

    # Just to save characters and fit everything on one line.
    pn = phone_number

    # remove commonly seen punctuation arround phone numbers.
    for char in (' ', '(', ')', '-', '.'):
        pn = pn.replace(char, '')

    if len(pn) == 11 and pn[0] == '1':
        pn = pn[1:]

    if re.match(re_number, pn):

        new_phone = '(' + pn[:3] + ') ' + pn[3:6] + '-' + pn[6:]
        return True, new_phone
    else:
        return False, 'invalid format'


def validate_account_number(account_number):
    ''' Validate the account number using the following rule: The sum of the
        first, third and fifth digits must be equal to the seventh and eighth
        digits.

        Return a tuple of a boolean and a status message. The boolean returns
        True if the param is valid, False otherwise. The status message
        explains the issue when returning False.
    '''

    re_account_number = '^\d{8}(\d)*$'
    an_str = str(account_number)

    if not re.match(re_account_number, an_str):
        return False, 'invalid account number'

    # Check account formula
    if not int(an_str[0]) + int(an_str[2]) + int(an_str[4]) == int(an_str[6:8]):
        return False, 'invalid account number'

    return True, account_number
