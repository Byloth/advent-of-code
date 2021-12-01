#!/usr/bin/env python

import unittest

from solution import parse_content, count_depths, get_window, get_all_windows, sum_windows


TEST_INPUT = """199
200
208
210
200
207
240
269
260
263"""


class TestSolution(unittest.TestCase):
    numbers = None

    def setUp(self):
        self.numbers = parse_content(TEST_INPUT)

    def test_get_window(self):
        window = get_window(self.numbers, 4, 4)

        self.assertEqual(window, [200, 207, 240, 269])

    def test_get_all_windows_sums(self):
        sums = [el for el in sum_windows(get_all_windows(self.numbers, 5))]

        self.assertEqual(sums, [1017, 1025, 1065, 1126, 1176, 1239])

    def test_count_depths(self):
        count = count_depths(self.numbers)

        self.assertEqual(count, 7)


if __name__ == "__main__":
    unittest.main()
