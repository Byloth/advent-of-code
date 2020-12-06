#!/usr/bin/env python


def parse_line(line):
    return line.split("\n")


def parse_input(input):
    lines = input.split("\n\n")
    lines = map(parse_line, lines)

    return list(lines)


def read_input(filename):
    with open(filename) as file:
        content = file.read()

    return parse_input(content)


def count_any_positive_answers(group):
    result = set()

    for answer in group:
        result |= set(answer)

    return len(result)


def count_all_positive_answers(group):
    result = set()

    for index, answer in enumerate(group):
        if index == 0:
            result = set(answer)

        else:
            result &= set(answer)

    return len(result)


if __name__ == "__main__":
    groups = read_input('input.txt')

    first = sum(count_any_positive_answers(group) for group in groups)
    print(first)

    second = sum(count_all_positive_answers(group) for group in groups)
    print(second)
