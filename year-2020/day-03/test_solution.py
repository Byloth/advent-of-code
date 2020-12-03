#!/usr/bin/env python

import unittest

from solution import SLOPES, parse_input, count_trees, multiply_all_trees


INPUT = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


class TestSolution(unittest.TestCase):
    trees = None

    def setUp(self):
        self.trees = parse_input(INPUT)

    def test_count_1_1_trees(self):
        self.assertEqual(count_trees(self.trees, 1, 1), 2)

    def test_count_3_1_trees(self):
        self.assertEqual(count_trees(self.trees, 3, 1), 7)

    def test_count_5_1_trees(self):
        self.assertEqual(count_trees(self.trees, 5, 1), 3)

    def test_count_7_1_trees(self):
        self.assertEqual(count_trees(self.trees, 7, 1), 4)

    def test_count_1_2_trees(self):
        self.assertEqual(count_trees(self.trees, 1, 2), 2)

    def test_multiply_all_trees(self):
        self.assertEqual(multiply_all_trees(self.trees, SLOPES), 336)


if __name__ == "__main__":
    unittest.main()
