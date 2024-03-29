#!/usr/bin/env python

def mul(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


def parse_content(content):
    lines = content.split("\n")

    return [int(line) for line in lines]


def read_file(filename):
    with open(filename) as file:
        content = file.read()

    return parse_content(content)


def get_matches(numbers, combinations, total, pointer = 0):
    index = pointer
    length = len(numbers)

    while index < length:
        number = numbers[index]
        match = total - number

        if combinations == 2:
            if match in numbers:
                return [number, match]

        else:
            matches = get_matches(numbers, combinations - 1, match, pointer = (index + 1))

            if matches:
                return [number, *matches]

        index += 1


if __name__ == "__main__":
    numbers = read_file('input.txt')

    first = mul(get_matches(numbers, 2, 2020))
    print(first)

    second = mul(get_matches(numbers, 3, 2020))
    print(second)
