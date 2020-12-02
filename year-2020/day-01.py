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
            matches = get_matches(numbers, combinations - 1, match, index + 1)

            if matches:
                return [number, *matches]

        index += 1


if __name__ == "__main__":
    numbers = read_input('input.txt')

    first = get_matches(numbers, 2, 2020)
    print(f"{first} -> {mul(first)}")
    
    second = get_matches(numbers, 3, 2020)
    print(f"{second} -> {mul(second)}")
    
    # third = get_matches(numbers, 4, 2020)
    # print(f"{third} -> {mul(third)}")
    
    # fourth = get_matches(numbers, 5, 2020)
    # print(f"{fourth} -> {mul(fourth)}")
