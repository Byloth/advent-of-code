#!/usr/bin/env python

import unittest

from solution import parse_content, get_highest_seat


TEST_INPUT = """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""


class TestSolution(unittest.TestCase):
    seats = None

    def setUp(self):
        self.seats = parse_content(TEST_INPUT)

    def test_get_first_seat_id(self):
        self.assertEqual(self.seats[0], 357)

    def test_get_second_seat_id(self):
        self.assertEqual(self.seats[1], 567)

    def test_get_third_seat_id(self):
        self.assertEqual(self.seats[2], 119)

    def test_get_fourth_seat_id(self):
        self.assertEqual(self.seats[3], 820)

    def test_get_highest_seat_id(self):
        self.assertEqual(get_highest_seat(self.seats), 820)


if __name__ == "__main__":
    unittest.main()
