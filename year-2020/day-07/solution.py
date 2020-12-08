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


def parse_input(input):
    lines = input.split("\n")
    lines = map(parse_line, lines)

    result = {}

    for color, children in lines:
        result[color] = {
            'children': children,
            'parents': {}
        }

    return result


def compose_input(input):
    input = parse_input(input)

    for parent_color, parent in input.items():
        for child_color, child in parent['children'].items():
            instance = input[child_color]
            child['instance'] = instance
            instance['parents'][parent_color] = parent

    return input


def read_input(filename):
    with open(filename) as file:
        content = file.read()

    return compose_input(content)


def get_parents_of_bag(bag):
    parents = set()

    for color, parent in bag['parents'].items():
        parents.add(color)

        if parent['parents']:
            parents |= get_parents_of_bag(parent)

    return parents


def count_all_bags_in_bag(bag):
    count = 1

    for child in bag['children'].values():
        weight = child['count']
        instance = child['instance']

        count += count_all_bags_in_bag(instance) * weight

    return count


if __name__ == "__main__":
    bags = read_input('input.txt')

    first = len(get_parents_of_bag(bags["shiny gold"]))
    print(first)

    second = count_all_bags_in_bag(bags["shiny gold"]) - 1
    print(second)
