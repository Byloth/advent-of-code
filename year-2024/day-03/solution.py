#!/usr/bin/env python

import re


MUL_REGEX = re.compile("mul\\((\\d+),(\\d+)\\)")
ENABLED_MUL_REGEX = re.compile("do\\(\\)|don't\\(\\)|mul\\((\\d+),(\\d+)\\)")


def read_file(filename: str) -> list[tuple[int, int]]:
    with open(filename, encoding="utf-8") as file:
        content: str = file.read()

    return content


def get_mul_instructions(content):
    for regex_match in MUL_REGEX.finditer(content):
        yield regex_match


def get_enabled_mul_instructions(content):
    enabled = True
    for regex_match in ENABLED_MUL_REGEX.finditer(content):
        match regex_match.group():
            case "do()":
                enabled = True

            case "don't()":
                enabled = False

            case _:
                if enabled:
                    yield regex_match


def extract_numbers(instructions):
    for instruction in instructions:
        yield int(instruction.group(1)), int(instruction.group(2))


def multiply(numbers):
    for left, right in numbers:
        yield left * right

def main():
    content = read_file('input.txt')
    instructions = get_mul_instructions(content)
    numbers = extract_numbers(instructions)
    multiplications = multiply(numbers)

    first = sum(multiplications)

    print(first)

    instructions = get_enabled_mul_instructions(content)
    numbers = extract_numbers(instructions)
    multiplications = multiply(numbers)

    second = sum(multiplications)

    print(second)

if __name__ == "__main__":
    main()
