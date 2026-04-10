#!/usr/bin/env python

def parse_line(line):
    return line.split("\n")


def parse_content(content: str):
    lines = content.split("\n\n")
    lines = map(parse_line, lines)

    return list(lines)


def read_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return parse_content(content)


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


def main():
    groups = read_file('./input.txt')

    first = sum(count_any_positive_answers(group) for group in groups)
    print("Solution part 1:", first)

    second = sum(count_all_positive_answers(group) for group in groups)
    print("Solution part 2:", second)


if __name__ == "__main__":
    main()
