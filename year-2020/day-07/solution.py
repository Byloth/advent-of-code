#!/usr/bin/env python

import re

MATCH_REGEX = re.compile('^(.*?) bags contain (.*?)\\.$')
REPLACE_REGEX = re.compile(' bags?')


def parse_line(line):
    matches = MATCH_REGEX.match(line)
    parent = matches[1]
    content = matches[2]

    children = {}

    if content != "no other bags":
        bags = content.split(", ")

        for bag in bags:
            bag = REPLACE_REGEX.sub("", bag)
            count, child = bag.split(" ", 1)

            children[child] = { 'count': int(count) }

    return parent, children


def parse_content(content):
    lines = content.split("\n")
    lines = map(parse_line, lines)

    result = {}

    for color, children in lines:
        result[color] = {
            'children': children,
            'parents': {}
        }

    return result


def read_file(filename):
    with open(filename) as file:
        content = file.read()

    return parse_content(content)


def compute_children_and_parents(bags):
    for parent_color, parent_instance in bags.items():
        for child_color, child_detail in parent_instance['children'].items():
            child_instance = bags[child_color]
            child_detail['instance'] = child_instance
            child_instance['parents'][parent_color] = parent_instance

    return bags


def get_parents_of_bag(bag):
    parents = set()

    for color, parent in bag['parents'].items():
        parents.add(color)

        if parent['parents']:
            parents |= get_parents_of_bag(parent)

    return parents


def count_all_bags_in_bag(bag, initial_count = 0):
    count = initial_count

    for child in bag['children'].values():
        weight = child['count']
        instance = child['instance']

        count += count_all_bags_in_bag(instance, initial_count = 1) * weight

    return count


if __name__ == "__main__":
    bags = read_file('input.txt')
    bags = compute_children_and_parents(bags)

    first = len(get_parents_of_bag(bags["shiny gold"]))
    print(first)

    second = count_all_bags_in_bag(bags["shiny gold"])
    print(second)
