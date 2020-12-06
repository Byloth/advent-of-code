#!/usr/bin/env python

import unittest

from solution import parse_input, count_any_positive_answers, count_all_positive_answers


INPUT = """abc

a
b
c

ab
ac

a
a
a
a

b"""


class TestSolution(unittest.TestCase):
    groups = None

    def setUp(self):
        self.groups = parse_input(INPUT)

    def test_count_first_any_positive_answers(self):
        self.assertEqual(count_any_positive_answers(self.groups[0]), 3)

    def test_count_second_any_positive_answers(self):
        self.assertEqual(count_any_positive_answers(self.groups[1]), 3)

    def test_count_third_any_positive_answers(self):
        self.assertEqual(count_any_positive_answers(self.groups[2]), 3)

    def test_count_fourth_any_positive_answers(self):
        self.assertEqual(count_any_positive_answers(self.groups[3]), 1)

    def test_count_fifth_any_positive_answers(self):
        self.assertEqual(count_any_positive_answers(self.groups[4]), 1)

    def test_sum_any_positive_answers(self):
        self.assertEqual(sum(count_any_positive_answers(group) for group in self.groups), 11)

    def test_count_first_all_positive_answers(self):
        self.assertEqual(count_all_positive_answers(self.groups[0]), 3)

    def test_count_second_all_positive_answers(self):
        self.assertEqual(count_all_positive_answers(self.groups[1]), 0)

    def test_count_third_all_positive_answers(self):
        self.assertEqual(count_all_positive_answers(self.groups[2]), 1)

    def test_count_fourth_all_positive_answers(self):
        self.assertEqual(count_all_positive_answers(self.groups[3]), 1)

    def test_count_fifth_all_positive_answers(self):
        self.assertEqual(count_all_positive_answers(self.groups[4]), 1)

    def test_sum_all_positive_answers(self):
        self.assertEqual(sum(count_all_positive_answers(group) for group in self.groups), 6)


if __name__ == "__main__":
    unittest.main()
