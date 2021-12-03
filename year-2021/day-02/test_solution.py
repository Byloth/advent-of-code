#!/usr/bin/env python

import unittest

from solution import parse_content, navigate_simple, navigate_aim


TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class TestSolution(unittest.TestCase):
    course = None

    def setUp(self):
        self.course = parse_content(TEST_INPUT)

    def test_navigate_simple(self):
        coordinates = navigate_simple(self.course)

        self.assertEqual(coordinates, (15, 10))

    def test_navigate_aim(self):
        coordinates = navigate_aim(self.course)

        self.assertEqual(coordinates, (15, 60))


if __name__ == "__main__":
    unittest.main()
