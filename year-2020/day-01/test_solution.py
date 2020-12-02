#!/usr/bin/env python

import unittest

from solution import mul, read_input, get_matches


class TestSolution(unittest.TestCase):
    def test_get_matches(self):
        numbers = read_input('test_input.txt')

        self.assertEqual(mul(get_matches(numbers, 2, 2020)), 514579)
        self.assertEqual(mul(get_matches(numbers, 3, 2020)), 241861950)

if __name__ == "__main__":
    unittest.main()
