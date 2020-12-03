#!/usr/bin/env python

import unittest

from solution import parse_input, count_trees


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

    def test_count_trees(self):
        self.assertEqual(count_trees(self.trees, 3, 1), 7)



if __name__ == "__main__":
    unittest.main()
