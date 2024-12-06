#!/usr/bin/env python

from functools import partial


def parse_line(line: str) -> tuple[int, int]:
    left, right = line.split("   ")

    return int(left), int(right)


def parse_content(content: str) -> list[tuple[int, int]]:
    lines: list[str] = content.split("\n")

    return [parse_line(line) for line in lines]


def read_file(filename: str) -> list[tuple[int, int]]:
    with open(filename, encoding="utf-8") as file:
        content: str = file.read()

    return parse_content(content)


def split_columns(rows: list[tuple[int, int]]):
    left_column: list[int] = []
    right_column: list[int] = []

    for left, right in rows:
        left_column.append(left)
        right_column.append(right)

    return left_column, right_column


def compute_similarity(left_column: list[int], right_column: list[int]):
    occurrencies = {}
    similarity = 0

    for left in left_column:
        if left in occurrencies:
            similarity += occurrencies[left]

            continue
    
        filter_fn = partial(lambda x, y: x == y, left)
        filtered_rows = filter(filter_fn, right_column)
        count = len(list(filtered_rows))

        addend = count * left

        occurrencies[left] = addend
        similarity += addend

    return similarity


def difference_columns(left_column: list[int], right_column: list[int]):
    for left, right in zip(left_column, right_column):
        yield abs(left - right)


def main():
    rows = read_file('input.txt')
    left, right = split_columns(rows)

    left.sort()
    right.sort()

    difference = difference_columns(left, right)

    first = sum(difference)

    print(first)

    second = compute_similarity(left, right)

    print(second)


if __name__ == "__main__":
    main()
