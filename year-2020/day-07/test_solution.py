#!/usr/bin/env python

import unittest

from solution import parse_content, compute_children_and_parents, get_parents_of_bag, count_all_bags_in_bag


TEST_INPUT_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


TEST_INPUT_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


class TestSolution(unittest.TestCase):
    def test_count_all_parents_of_shiny_gold_bag(self):
        bags = parse_content(TEST_INPUT_1)
        bags = compute_children_and_parents(bags)

        self.assertEqual(len(get_parents_of_bag(bags["shiny gold"])), 4)

    def test_first_count_all_bags_in_bag(self):
        bags = parse_content(TEST_INPUT_1)
        bags = compute_children_and_parents(bags)

        self.assertEqual(count_all_bags_in_bag(bags["shiny gold"]), 32)

    def test_second_count_all_bags_in_bag(self):
        bags = parse_content(TEST_INPUT_2)
        bags = compute_children_and_parents(bags)

        self.assertEqual(count_all_bags_in_bag(bags["shiny gold"]), 126)


if __name__ == "__main__":
    unittest.main()
