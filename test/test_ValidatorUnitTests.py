#!/usr/bin/python2.7
""" Validator Class Unit Tests. These unit tests make sure that the functions
    in the Validator package are operating as expected.

"""

# Native modules
import unittest

# Custom python modules
import valapi.handlers.lib.Validator as lv


class ValidatorUnitTests(unittest.TestCase):

    def test_name_empty_returns_false(self):
        '''Test name as empty string returns.'''
        (result, status_message) = lv.validate_name('')
        self.assertFalse(result)

    def test_any_name_returns_true(self):
        '''Test name as random name returns.'''
        (result, status_message) = lv.validate_name('Random Name')
        self.assertTrue(result)

    def test_name_returns_a_capitalized_name(self):
        '''Test name capitalizes string returns.'''
        (result, status_message) = lv.validate_name('abraham')
        self.assertTrue(result)
        self.assertEqual('Abraham', status_message)

    def test_name_does_not_change_case(self):
        '''Test name does not change case after validation.'''
        (result, status_message) = lv.validate_name('McIntyre')
        self.assertTrue(result)
        self.assertEqual('McIntyre', status_message)

    def test_name_returns_a_capitalized_name_2(self):
        '''Test name as empty string returns format 2.'''
        (result, status_message) = lv.validate_name('abraham lincoln')
        self.assertTrue(result)
        self.assertEqual('Abraham Lincoln', status_message)

    def test_correct_dob_with_slash_is_accepted(self):
        '''Test correct DOB with slashes is valid'''
        (result, status_message) = lv.validate_dob('08/04/1961')
        self.assertTrue(result)

    def test_correct_dob_with_hyphen_is_accepted(self):
        '''Test correct DOB with hyphen is valid'''
        (result, status_message) = lv.validate_dob('08-04-1961')
        self.assertTrue(result)

    def test_correct_dob_with_dot_is_accepted(self):
        '''Test correct DOB with dot is valid'''
        (result, status_message) = lv.validate_dob('08.04.1961')
        self.assertTrue(result)

    def test_correct_dob_with_slash_and_2_digit_year_is_accepted(self):
        '''Test correct DOB with slashes is valid'''
        (result, status_message) = lv.validate_dob('08/04/61')
        self.assertTrue(result)

    def test_correct_dob_with_hyphen_and_2_digit_year_is_accepted(self):
        '''Test correct DOB with hyphen is valid'''
        (result, status_message) = lv.validate_dob('08-04-61')
        self.assertTrue(result)

    def test_correct_dob_with_dot_and_2_digit_year_is_accepted(self):
        '''Test correct DOB with dot is valid'''
        (result, status_message) = lv.validate_dob('08.04.61')
        self.assertTrue(result)

    def test_correct_dob_with_2_digit_year_returns_4_digit_year(self):
        '''Test correct DOB with 2 digit dot is valid and returns 4 digit year'''
        (result, status_message) = lv.validate_dob('08.04.61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_0(self):
        '''Test correct DOB with various format 0'''
        (result, status_message) = lv.validate_dob('8.4.61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_1(self):
        '''Test correct DOB with various format 1'''
        (result, status_message) = lv.validate_dob('8.4.1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_2(self):
        '''Test correct DOB with various format 2'''
        (result, status_message) = lv.validate_dob('8.04.61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_3(self):
        '''Test correct DOB with various format 3'''
        (result, status_message) = lv.validate_dob('8.04.1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_4(self):
        '''Test correct DOB with various format 4'''
        (result, status_message) = lv.validate_dob('08.4.61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_5(self):
        '''Test correct DOB with various format 5'''
        (result, status_message) = lv.validate_dob('08.4.1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_6(self):
        '''Test correct DOB with various format 6'''
        (result, status_message) = lv.validate_dob('08.04.61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_7(self):
        '''Test correct DOB with various format 7'''
        (result, status_message) = lv.validate_dob('08.04.1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_8(self):
        '''Test correct DOB with various format 8'''
        (result, status_message) = lv.validate_dob('8/4/61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_9(self):
        '''Test correct DOB with various format 9'''
        (result, status_message) = lv.validate_dob('8/4/1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_10(self):
        '''Test correct DOB with various format 10'''
        (result, status_message) = lv.validate_dob('8/04/61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_11(self):
        '''Test correct DOB with various format 11'''
        (result, status_message) = lv.validate_dob('8/04/1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_12(self):
        '''Test correct DOB with various format 12'''
        (result, status_message) = lv.validate_dob('08/4/61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_13(self):
        '''Test correct DOB with various format 13'''
        (result, status_message) = lv.validate_dob('08/4/1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_14(self):
        '''Test correct DOB with various format 14'''
        (result, status_message) = lv.validate_dob('08/04/61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_15(self):
        '''Test correct DOB with various format 15'''
        (result, status_message) = lv.validate_dob('08/04/1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_16(self):
        '''Test correct DOB with various format 16'''
        (result, status_message) = lv.validate_dob('8-4-61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_17(self):
        '''Test correct DOB with various format 17'''
        (result, status_message) = lv.validate_dob('8-4-1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_18(self):
        '''Test correct DOB with various format 18'''
        (result, status_message) = lv.validate_dob('8-04-61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_19(self):
        '''Test correct DOB with various format 19'''
        (result, status_message) = lv.validate_dob('8-04-1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_20(self):
        '''Test correct DOB with various format 20'''
        (result, status_message) = lv.validate_dob('08-4-61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_21(self):
        '''Test correct DOB with various format 21'''
        (result, status_message) = lv.validate_dob('08-4-1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_22(self):
        '''Test correct DOB with various format 22'''
        (result, status_message) = lv.validate_dob('08-04-61')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_correct_dob_various_format_23(self):
        '''Test correct DOB with various format 23'''
        (result, status_message) = lv.validate_dob('08-04-1961')
        self.assertTrue(result)
        self.assertEqual('08/04/1961', status_message)

    def test_person_dob_too_young_status_message(self):
        '''Test a status_message is returned DOB is invalid'''
        (result, status_message) = lv.validate_dob('08/04/2015')
        self.assertEqual('person too young', status_message)

    def test_person_dob_too_old_status_message_2_digit_year(self):
        '''Test a status_message is returned DOB is invalid'''
        (result, status_message) = lv.validate_dob('08/04/01')
        self.assertEqual('person too old', status_message)

    def test_person_dob_too_old_status_message(self):
        '''Test a status_message is returned DOB is invalid'''
        (result, status_message) = lv.validate_dob('08/04/1715')
        self.assertEqual('person too old', status_message)

    def test_5_digit_zip_code_is_accepted(self):
        '''Test that a 5 digit zip code is accepted.'''
        (result, status_message) = lv.validate_zip_code('12345')
        self.assertTrue(result)

    def test_9_digit_zip_code_is_accepted(self):
        '''Test that a 9 digit zip code is accepted.'''
        (result, status_message) = lv.validate_zip_code('123456789')
        self.assertTrue(result)

    def test_6_digit_zip_code_is_not_accepted(self):
        '''Test that a 6 digit zip code is not accepted.'''
        (result, status_message) = lv.validate_zip_code('123456')
        self.assertFalse(result)

    def test_4_digit_zip_code_is_not_accepted(self):
        '''Test that a 4 digit zip code is not accepted.'''
        (result, status_message) = lv.validate_zip_code('1234')
        self.assertFalse(result)

    def test_10_digit_zip_code_is_not_accepted(self):
        '''Test that a 10 digit zip code is not accepted.'''
        (result, status_message) = lv.validate_zip_code('1234567890')
        self.assertFalse(result)

    def test_5_letters_for_zip_code_is_not_accepted(self):
        '''Test that a 5 letters zip code is not accepted.'''
        (result, status_message) = lv.validate_zip_code('abcde')
        self.assertFalse(result)

    def test_invalid_zip_code_returns_status_message(self):
        '''Test that an invalid zip code returns a status message.'''
        (result, status_message) = lv.validate_zip_code('abcde')
        self.assertEqual('invalid format', status_message)

    def test_valid_zip_code_returns_formatted_zip_code_format_1(self):
        '''Test that a valid zip code format 1 returns a well formated zip code.'''
        (result, status_message) = lv.validate_zip_code('12345-1234')
        self.assertTrue(result)
        self.assertEqual('12345-1234', status_message)

    def test_valid_zip_code_returns_formatted_zip_code_format_2(self):
        '''Test that a valid zip code format 2 returns a well formated zip code.'''
        (result, status_message) = lv.validate_zip_code('123451234')
        self.assertTrue(result)
        self.assertEqual('12345-1234', status_message)

    def test_valid_zip_code_returns_formatted_zip_code_format_3(self):
        '''Test that a valid zip code format 3 returns a well formated zip code.'''
        (result, status_message) = lv.validate_zip_code('12345')
        self.assertTrue(result)
        self.assertEqual('12345', status_message)

    def test_valid_zip_code_returns_formatted_zip_code_format_4(self):
        '''Test that valid zip code format 4 returns a well formated zip code.'''
        (result, status_message) = lv.validate_zip_code('12345 - 1234')
        self.assertTrue(result)
        self.assertEqual('12345-1234', status_message)

    def test_valid_zip_code_returns_formatted_zip_code_format_5(self):
        '''Test that valid zip code format 5 returns a well formated zip code.'''
        (result, status_message) = lv.validate_zip_code('12345 1234')
        self.assertTrue(result)
        self.assertEqual('12345-1234', status_message)

    def test_10_digit_phone_number_is_accepted(self):
        '''Test that a 10 digit phone number is accepted.'''
        (result, status_message) = lv.validate_phone_number('9087654321')
        self.assertTrue(result)

    def test_10_digit_phone_number_format_1_is_accepted(self):
        '''Test that a 10 digit phone number with format 1 is accepted.'''
        (result, status_message) = lv.validate_phone_number('(908)765-4321')
        self.assertTrue(result)

    def test_10_digit_phone_number_format_2_is_accepted(self):
        '''Test that a 10 digit phone number with format 2 is accepted.'''
        (result, status_message) = lv.validate_phone_number('1(908)765-4321')
        self.assertTrue(result)

    def test_10_digit_phone_number_format_3_is_accepted(self):
        '''Test that a 10 digit phone number with format 3 is accepted.'''
        (result, status_message) = lv.validate_phone_number('908.765.4321')
        self.assertTrue(result)

    def test_10_digit_phone_number_format_4_is_accepted(self):
        '''Test that a 10 digit phone number with format 4 is accepted.'''
        (result, status_message) = lv.validate_phone_number('908-765-4321')
        self.assertTrue(result)

    def test_11_digit_phone_number_format_5_is_accepted(self):
        '''Test that a 10 digit phone number with format 5 is accepted.'''
        (result, status_message) = lv.validate_phone_number('1-908-765-4321')
        self.assertTrue(result)

    def test_12_digit_phone_number_format_6_is_accepted(self):
        '''Test that a 12 digit phone number with format 6 is accepted.'''
        (result, status_message) = lv.validate_phone_number('1-908-765-43211')
        self.assertFalse(result)

    def test_11_digit_phone_number_with_1_is_accepted(self):
        '''Test that a 11 digit phone number starting with 1 is accepted.'''
        (result, status_message) = lv.validate_phone_number('19087654321')
        self.assertTrue(result)

    def test_11_digit_phone_number_without_1_is_not_accepted(self):
        ''' Test that a 11 digit phone number starting without 1 is not
            accepted.
        '''
        (result, status_message) = lv.validate_phone_number('29087654321')
        self.assertFalse(result)

    def test_9_digit_phone_number_is_not_accepted(self):
        ''' Test that a 9 digit phone number is not accepted.'''
        (result, status_message) = lv.validate_phone_number('987654321')
        self.assertFalse(result)

    def test_12_digit_phone_number_is_not_accepted(self):
        ''' Test that a 12 digit phone number is not accepted.'''
        (result, status_message) = lv.validate_phone_number('98765432100')
        self.assertFalse(result)

    def test_10_letters_phone_number_is_not_accepted(self):
        ''' Test that a 10 letters phone number is not accepted.'''
        (result, status_message) = lv.validate_phone_number('800inscred')
        self.assertFalse(result)

    def test_invalid_phone_number_returns_status_message(self):
        '''Test that an invalid phone number returns a status message.'''
        (result, status_message) = lv.validate_phone_number('800badnum')
        self.assertEqual('invalid format', status_message)

    def test_invalid_account_number_is_not_accepted(self):
        '''Tests that an invalid account number fails.'''
        (result, status_message) = lv.validate_account_number(12942311)
        self.assertFalse(result)

    def test_invalid_account_number_returns_status_message(self):
        '''Tests that an invalid account number fails.'''
        (result, status_message) = lv.validate_account_number(12942311)
        self.assertEqual('invalid account number', status_message)

    def test_valid_account_number_is_accepted(self):
        '''Tests that a valid account number is accepteds.'''
        (result, status_message) = lv.validate_account_number(42942315)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
