#!/usr/bin/env python


def parse_content(content):
    lines = content.split("\n")
    lines = map(lambda line: int(line), lines)
    
    return list(lines)


def read_file(filename):
    with open(filename) as file:
        content = file.read()

    return parse_content(content)


def is_number_valid(number, numbers, start, end):
    for i in range(start, end):
        first = numbers[i]

        for j in range(i + 1, end):
            second = numbers[j]

            if (first + second) == number:
                return True

    return False


def get_first_invalid_line(numbers, preamble):
    length = len(numbers)

    start = 0
    pointer = preamble

    while pointer < length:
        number = numbers[pointer]

        if not is_number_valid(number, numbers, start, pointer):
            return number

        start += 1
        pointer += 1

    return False


def get_contiguous_range_of_sum(sum_to_find, numbers):
    pointer = 0
    length = len(numbers)

    while pointer < length:
        index = pointer
        result = numbers[index]
        
        while result < sum_to_find:
            index += 1
            result += numbers[index]

        if result == sum_to_find:
            return pointer, index

        pointer += 1


def get_smaller_and_greater(numbers, start, end):
    minimum = numbers[start]
    maximum = numbers[start]

    for index in range(start + 1, end):
        minimum = min(minimum, numbers[index])
        maximum = max(maximum, numbers[index])

    return minimum, maximum


if __name__ == "__main__":
    numbers = read_file('input.txt')

    first = get_first_invalid_line(numbers, 25)
    print(first)

    start, end = get_contiguous_range_of_sum(first, numbers)
    second = sum(get_smaller_and_greater(numbers, start, end))
    print(second)
