#!/usr/bin/env python

def parse_content(content: str):
    lines = content.split("\n")

    return [int(line) for line in lines]


def read_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return parse_content(content)


def get_window(numbers, start, width):
    end = start + width

    return numbers[start:end]


def get_all_windows(numbers, width):
    length = len(numbers) - (width - 1)

    for index in range(length):
        yield get_window(numbers, index, width)


def sum_windows(windows):
    for window in windows:
        yield sum(window)


def count_depths(numbers):
    count = 0
    previous_number = numbers[0]

    for number in numbers:
        if number > previous_number:
            count += 1

        previous_number = number

    return count


def main():
    numbers = read_file('./input.txt')
    first = count_depths(numbers)
    print("Solution part 1:", first)

    windows = get_all_windows(numbers, 3)
    sums = list(sum_windows(windows))
    second = count_depths(sums)
    print("Solution part 2:", second)


if __name__ == "__main__":
    main()
