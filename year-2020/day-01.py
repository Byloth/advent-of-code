#!/usr/bin/python


def mul(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


def read_input(filename):
    with open(filename) as file:
        content = file.read()

    lines = content.split("\n")

    return [int(line) for line in lines]


def get_matches(numbers, combinations, total):
    for number in numbers:
        match = total - number
        others = [other for other in numbers if other != number]

        if combinations == 2:
            if match in others:
                return [number, match]

        else:
            matches = get_matches(others, combinations - 1, match)

            if matches:
                return [number, *matches]


if __name__ == "__main__":
    numbers = read_input('input.txt')

    first = get_matches(numbers, 2, 2020)
    print(f"{first} -> {mul(first)}")
    
    second = get_matches(numbers, 3, 2020)
    print(f"{second} -> {mul(second)}")
