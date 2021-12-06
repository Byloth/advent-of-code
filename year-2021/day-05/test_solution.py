#!/usr/bin/env python

import unittest

from solution import parse_content


TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class TestSolution(unittest.TestCase):
    rows = None

    def setUp(self):
        self.rows = parse_content(TEST_INPUT)


if __name__ == "__main__":
    unittest.main()
