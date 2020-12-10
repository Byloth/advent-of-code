#!/usr/bin/env python

import unittest

from solution import parse_content, execute, fix_and_execute


TEST_INPUT = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


class TestSolution(unittest.TestCase):
    program = None

    def setUp(self):
        self.program = parse_content(TEST_INPUT)

    def test_execute(self):
        self.assertEqual(execute(self.program), (5, 1))

    def test_fix_and_execute(self):
        self.assertEqual(fix_and_execute(self.program), 8)


if __name__ == "__main__":
    unittest.main()
