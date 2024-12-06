#!/usr/bin/env python

import unittest

from solution import parse_content, split_columns, difference_columns, compute_similarity

TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


class TestSolution(unittest.TestCase):
    rows = None

    def setUp(self):
        self.rows = parse_content(TEST_INPUT)

    def test_split_columns(self):
        left, right = split_columns(self.rows)

        self.assertEqual(left, [3, 4, 2, 1, 3, 3])
        self.assertEqual(right, [4, 3, 5, 3, 9, 3])

    def test_difference_columns(self):
        left, right = split_columns(self.rows)
        
        left.sort()
        right.sort()

        difference = difference_columns(left, right)
        total = sum(difference)

        self.assertEqual(total, 11)

    def test_compute_similarity(self):
        left, right = split_columns(self.rows)
        similarity = compute_similarity(left, right)

        self.assertEqual(similarity, 31)


if __name__ == "__main__":
    unittest.main()
