#!/usr/bin/env python

import unittest

from solution import parse_content, count_differences, count_arrangements


TEST_INPUT_1 = """16
10
15
5
1
11
7
19
6
12
4"""

TEST_INPUT_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


class TestSolution(unittest.TestCase):
    def test_count_first_differences(self):
        adapters = parse_content(TEST_INPUT_1)
        one, _, three = count_differences(adapters)

        self.assertEqual(one * three, 7 * 5)

    def test_count_second_differences(self):
        adapters = parse_content(TEST_INPUT_2)
        one, _, three = count_differences(adapters)

        self.assertEqual(one * three, 22 * 10)

    def test_count_first_arrangements(self):
        adapters = parse_content(TEST_INPUT_1)

        self.assertEqual(count_arrangements(adapters), 8)

    def test_count_second_arrangements(self):
        adapters = parse_content(TEST_INPUT_2)

        self.assertEqual(count_arrangements(adapters), 19208)


if __name__ == "__main__":
    unittest.main()
