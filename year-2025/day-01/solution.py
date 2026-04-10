#!/usr/bin/env python

def parse_content(content: str) -> list[tuple[str, int]]:
    instruction = []

    for line in content.split("\n"):
        direction = line[0]
        value = int(line[1:].strip())

        line = (direction, value)
        instruction.append(line)

    return instruction


def read_file(filename: str) -> list[tuple[str, int]]:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return parse_content(content)


def count_perfect_zeros(instructions: list[tuple[str, int]]) -> int:
    dial: int = 50
    password: int = 0

    for direction, value in instructions:
        if direction == "L":
            value = -(value)

        dial = dial % 100

        if dial == 0:
            password += 1

    return password


def count_passing_zeros(instructions: list[tuple[str, int]]) -> int:
    previous: int = 50
    dial: int = 50
    password: int = 0

    for direction, value in instructions:
        if direction == "L":
            value = -(value)

        dial += value
        ratio = dial / 100

        if ratio > 0:
            ratio = int(ratio)

        else:
            ratio = int(-(ratio))
            ratio += 1 if previous != 0 else 0

        password += ratio

        dial = dial % 100
        previous = dial

    return password


def main():
    lines = read_file("./input.txt")

    first = count_perfect_zeros(lines)
    print("Solution part 1:", first)

    second = count_passing_zeros(lines)
    print("Solution part 2:", second)


if __name__ == "__main__":
    main()
