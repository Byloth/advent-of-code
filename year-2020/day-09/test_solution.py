#!/usr/bin/env python

import unittest

from solution import parse_content, get_first_invalid_line, get_contiguous_range_of_sum, get_smaller_and_greater


TEST_INPUT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


class TestSolution(unittest.TestCase):
    numbers = None

    def setUp(self):
        self.numbers = parse_content(TEST_INPUT)

    def test_get_first_invalid_line(self):
        self.assertEqual(get_first_invalid_line(self.numbers, 5), 127)

    def test_get_contiguous_range_of_sum(self):
        self.assertEqual(get_contiguous_range_of_sum(127, self.numbers), (2, 5))

    def test_get_smaller_and_greater(self):
        self.assertEqual(get_smaller_and_greater(self.numbers, 2, 5), (15, 47))


if __name__ == "__main__":
    unittest.main()
