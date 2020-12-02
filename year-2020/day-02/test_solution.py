#!/usr/bin/env python

import unittest

from solution import read_input, min_max_valid_passwords, first_second_password_valid


class TestSolution(unittest.TestCase):
    def test_min_max_valid_passwords(self):
        passwords = read_input('test_input.txt')

        self.assertEqual(min_max_valid_passwords(passwords), 2)

    def test_first_second_password_valid(self):
        passwords = read_input('test_input.txt')

        self.assertEqual(first_second_password_valid(passwords), 1)

if __name__ == "__main__":
    unittest.main()
