#!/usr/bin/env python


def parse_line(line):
    return [True if char == '#' else False for char in line]


def parse_input(input):
    lines = input.split("\n")
    lines = map(parse_line, lines)

    return list(lines)
    

def read_input(filename):
    with open(filename) as file:
        content = file.read()

    return parse_input(content)


def count_trees(trees, addX, addY):
    lengthY = len(trees)
    lengthX = len(trees[0])

    x = 0
    y = 0
    count = 0

    while y < lengthY:
        if trees[y][x] == True:
            count += 1

        x = (x + addX) % lengthX
        y += addY

    return count


if __name__ == "__main__":
    trees = read_input('input.txt')

    first = count_trees(trees, 3, 1)
    print(first)

