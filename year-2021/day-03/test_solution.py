#!/usr/bin/env python

import unittest

from solution import parse_content, get_most_common_digits, inverse_binary_string, get_most_common_number, get_least_common_number


TEST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


class TestSolution(unittest.TestCase):
    rows = None

    def setUp(self):
        self.rows = parse_content(TEST_INPUT)

    def test_get_most_common_digits(self):
        self.assertEqual(get_most_common_digits(self.rows), "10110")
        self.assertEqual(int("10110", 2), 22)

    def test_inverse_binary_string(self):
        most_common_digits = get_most_common_digits(self.rows)
        
        self.assertEqual(inverse_binary_string(most_common_digits), "01001")
        self.assertEqual(int("01001", 2), 9)

    def test_get_most_common_number(self):
        self.assertEqual(get_most_common_number(self.rows), "10111")

    def get_least_common_number(self):
        self.assertEqual(get_least_common_number(self.rows), "01010")


if __name__ == "__main__":
    unittest.main()
