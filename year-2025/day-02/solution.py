#!/usr/bin/env python

from typing import Generator

TEST_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def parse_content(content: str) -> Generator[tuple[int, int], None, None]:
    couples = content.split(",")
    for couple in couples:
        limits = couple.split("-")

        yield int(limits[0]), int(limits[1])


def read_file(filename: str) -> Generator[tuple[str, int], None, None]:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return list(parse_content(content))


def split_and_check(value: str, parts = 2) -> bool:
    length = len(value)

    if length % parts != 0:
        return False

    part_length = int(length / parts)

    start = 0
    middle = part_length
    end = middle + part_length

    while end <= length:
        part1 = value[start:middle]
        part2 = value[middle:end]

        if part1 != part2:
            return False
        
        start = middle
        middle = end
        end = middle + part_length

    return True


def find_two_parts_invalid_ids(limits: Generator[tuple[str, int], None, None]) -> Generator[int, None, None]:
    for min_limit, max_limit in limits:
        numbers = range(min_limit, max_limit + 1)

        for number in numbers:
            value = str(number)

            if split_and_check(value):
                yield number


def find_multiple_parts_invalid_ids(limits: Generator[tuple[str, int], None, None]) -> Generator[int, None, None]:
    for min_limit, max_limit in limits:
        numbers = range(min_limit, max_limit + 1)

        for number in numbers:
            value = str(number)
            length = len(value)

            parts = 2
            while parts <= length:
                if split_and_check(value, parts):
                    yield number
                    break
            
                parts += 1


def main():
    lines = read_file("./input.txt")
    invalid_ids = find_two_parts_invalid_ids(lines)

    first = sum(invalid_ids)
    print("Solution part 1:", first)

    invalid_ids = find_multiple_parts_invalid_ids(lines)

    second = sum(invalid_ids)
    print("Solution part 2:", second)


if __name__ == "__main__":
    main()
