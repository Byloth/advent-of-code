#!/usr/bin/env python


def parse_content(content):
    return content.split("\n")


def read_file(filename):
    with open(filename) as file:
        content = file.read()

    return parse_content(content)


def get_most_common_digit_at_index(rows, index):
    count = {'1': 0, '0': 0}

    for row in rows:
        digit = row[index]
        count[digit] += 1

    return max(count, key=count.get)


def get_least_common_digit_at_index(rows, index):
    count = {'0': 0, '1': 0}

    for row in rows:
        digit = row[index]
        count[digit] += 1

    return min(count, key=count.get)


def filter_by_digit_at_index(rows, digit, index):
    return [row for row in rows if row[index] == digit]


def get_most_common_number(rows):
    index = 0

    while len(rows) > 1:
        digit = get_most_common_digit_at_index(rows, index)
        rows = filter_by_digit_at_index(rows, digit, index)

        index += 1

    return rows[0]


def get_least_common_number(rows):
    index = 0

    while len(rows) > 1:
        digit = get_least_common_digit_at_index(rows, index)
        rows = filter_by_digit_at_index(rows, digit, index)

        index += 1

    return rows[0]


def get_most_common_digits(rows):
    counts = []
    length = len(rows[0])

    for index in range(length):
        counts.append({'1': 0, '0': 0})

    for row in rows:
        for index, digit in enumerate(row):
            counts[index][digit] += 1

    digits = ""
    for count in counts:
        digits += max(count, key=count.get)

    return digits


def inverse_binary_string(value):
    digits = ""

    for digit in value:
        if digit == "1":
            digits += "0"

        else:
            digits += "1"

    return digits


def main():
    rows = read_file('input.txt')

    most_common_digits = get_most_common_digits(rows)
    least_common_digits = inverse_binary_string(most_common_digits)

    gamma_rate = int(most_common_digits, 2)
    epsilon_rate = int(least_common_digits, 2)

    first = gamma_rate * epsilon_rate

    print(first)

    oxigen_rating = int(get_most_common_number(rows), 2)
    co2_rating = int(get_least_common_number(rows), 2)

    second = oxigen_rating * co2_rating

    print(second)


if __name__ == "__main__":
    main()
