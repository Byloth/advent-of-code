#!/usr/bin/env python

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


def parse_line(line):
    return [(char == '#') for char in line]


def parse_content(content: str):
    lines = content.split("\n")
    lines = map(parse_line, lines)

    return list(lines)


def read_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return parse_content(content)


def count_trees(trees, add_x, add_y):
    length_y = len(trees)
    length_x = len(trees[0])

    x = 0
    y = 0
    count = 0

    while y < length_y:
        if trees[y][x] is True:
            count += 1

        x = (x + add_x) % length_x
        y += add_y

    return count


def multiply_all_trees(trees, slopes):
    result = 1

    for add_x, add_y in slopes:
        result *= count_trees(trees, add_x, add_y)

    return result


def main():
    trees = read_file('./input.txt')

    first = count_trees(trees, 3, 1)
    print("Solution part 1:", first)

    second = multiply_all_trees(trees, SLOPES)
    print("Solution part 2:", second)


if __name__ == "__main__":
    main()
