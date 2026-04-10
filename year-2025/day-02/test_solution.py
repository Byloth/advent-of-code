#!/usr/bin/env python

import unittest

from solution import parse_content, find_two_parts_invalid_ids, find_multiple_parts_invalid_ids


TEST_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


class TestSolution(unittest.TestCase):
    limits = None

    def setUp(self):
        self.limits = parse_content(TEST_INPUT)

    def test_part1(self):
        invalid_ids = find_two_parts_invalid_ids(self.limits)
        result = sum(invalid_ids)

        self.assertEqual(result, 1227775554)

    def test_part2(self):
        invalid_ids = find_multiple_parts_invalid_ids(self.limits)
        result = sum(invalid_ids)

        self.assertEqual(result, 4174379265)
