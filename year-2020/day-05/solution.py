#!/usr/bin/env python


def get_row(value):
    value = value.replace("F", "0") \
                 .replace("B", "1")

    return int(value, 2)


def get_column(value):
    value = value.replace("L", "0") \
                 .replace("R", "1")

    return int(value, 2)


def parse_line(line):
    row = get_row(line[:7])
    column = get_column(line[7:])

    return (row * 8) + column


def parse_input(input):
    lines = input.split("\n")
    lines = map(parse_line, lines)

    return list(lines)


def read_input(filename):
    with open(filename) as file:
        content = file.read()

    return parse_input(content)


def get_highest_seat(seats):
    maximum = 0

    for seat in seats:
        maximum = max(maximum, seat)

    return maximum


def find_missing_seat(seats):
    seats = sorted(seats)
    length = len(seats)
    value = seats[0]
    index = 1

    while (value + 1) == seats[index]:
        value = seats[index]
        index += 1

    return value + 1


if __name__ == "__main__":
    seats = read_input('input.txt')

    first = get_highest_seat(seats)
    print(first)

    second = find_missing_seat(seats)
    print(second)
