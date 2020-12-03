#!/usr/bin/env python

import unittest

from solution import parse_input, min_max_valid_passwords, first_second_password_valid


INPUT = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


class TestSolution(unittest.TestCase):
    passwords = None

    def setUp(self):
        self.passwords = parse_input(INPUT)

    def test_min_max_valid_passwords(self):
        self.assertEqual(min_max_valid_passwords(self.passwords), 2)

    def test_first_second_password_valid(self):
        self.assertEqual(first_second_password_valid(self.passwords), 1)


if __name__ == "__main__":
    unittest.main()
