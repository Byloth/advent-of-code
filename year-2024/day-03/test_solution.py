#!/usr/bin/env python

import unittest

from solution import get_mul_instructions, get_enabled_mul_instructions, extract_numbers, multiply

TEST_INPUT = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


class TestSolution(unittest.TestCase):
    def test_get_mul_instructions(self):
        instructions = get_mul_instructions(TEST_INPUT)
        multiplications = [match.group(0) for match in instructions]

        self.assertEqual(multiplications, ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)'])


    def test_get_enabled_mul_instructions(self):
        instructions = get_enabled_mul_instructions(TEST_INPUT)
        multiplications = [match.group(0) for match in instructions]

        self.assertEqual(multiplications, ['mul(2,4)', 'mul(8,5)'])


    def test_extract_numbers(self):
        instructions = get_mul_instructions(TEST_INPUT)
        numbers = list(extract_numbers(instructions))

        self.assertEqual(numbers, [(2, 4), (5, 5), (11, 8), (8, 5)])

    def test_multiply(self):
        instructions = get_mul_instructions(TEST_INPUT)
        numbers = list(extract_numbers(instructions))
        products = list(multiply(numbers))

        self.assertEqual(products, [8, 25, 88, 40])


if __name__ == "__main__":
    unittest.main()
