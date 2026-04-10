#!/usr/bin/env python

import unittest

from solution import parse_content, count_perfect_zeros, count_passing_zeros


TEST_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


class TestSolution(unittest.TestCase):
    instructions = None

    def setUp(self):
        self.instructions = parse_content(TEST_INPUT)

    def test_part1(self):
        count = count_perfect_zeros(self.instructions)
        self.assertEqual(count, 3)

    def test_part2(self):
        count = count_passing_zeros(self.instructions)
        self.assertEqual(count, 6)
