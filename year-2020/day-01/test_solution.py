#!/usr/bin/env python

import unittest

from solution import mul, parse_content, get_matches


TEST_INPUT = """1721
979
366
299
675
1456"""


class TestSolution(unittest.TestCase):
    numbers = None

    def setUp(self):
        self.numbers = parse_content(TEST_INPUT)

    def test_get_2_matches(self):
        self.assertEqual(mul(get_matches(self.numbers, 2, 2020)), 514579)

    def test_get_3_matches(self):
        self.assertEqual(mul(get_matches(self.numbers, 3, 2020)), 241861950)


if __name__ == "__main__":
    unittest.main()
