#!/usr/bin/env python

import unittest

from solution import parse_content, get_first_winning_values, get_last_winning_values, sum_unmarked_cells


TEST_INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class TestSolution(unittest.TestCase):
    numbers = None
    boards = None

    def setUp(self):
        self.numbers, self.boards = parse_content(TEST_INPUT)

    def test_get_first_winning_values(self):
        winning_number, winning_board = get_first_winning_values(self.numbers, self.boards)

        self.assertEqual(winning_number, 24)
        self.assertEqual(winning_board, self.boards[2])

    def test_get_last_winning_values(self):
        winning_number, winning_board = get_last_winning_values(self.numbers, self.boards)

        self.assertEqual(winning_number, 13)
        self.assertEqual(winning_board, self.boards[1])

    def test_sum_unmarked_cells(self):
        _, winning_board = get_first_winning_values(self.numbers, self.boards)

        self.assertEqual(sum_unmarked_cells(winning_board), 188)


if __name__ == "__main__":
    unittest.main()
