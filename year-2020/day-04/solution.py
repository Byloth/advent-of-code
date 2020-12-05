#!/usr/bin/env python

import re


COLOR_REGEX = re.compile('^#[0-9a-f]{6}$')
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
PASSPORT_REGEX = re.compile('^[0-9]{9}$')


def check_height(value):
    if value.endswith("cm"):
        height = int(value[:-2])

        return 150 <= height <= 193

    elif value.endswith("in"):
        height = int(value[:-2])

        return 59 <= height <= 76

    return False


PASSPORT_FIELDS = {
    'byr': lambda value: 1920 <= int(value) <= 2002,
    'iyr': lambda value: 2010 <= int(value) <= 2020,
    'eyr': lambda value: 2020 <= int(value) <= 2030,
    'hgt': check_height,
    'hcl': lambda value: COLOR_REGEX.match(value),
    'ecl': lambda value: value in EYE_COLORS,
    'pid': lambda value: PASSPORT_REGEX.match(value)
}


def parse_line(line):
    line = line.replace("\n", " ")
    parts = line.split(" ")

    result = {}
    for part in parts:
        key, value = part.split(":")

        result[key] = value

    return result


def parse_input(input):
    lines = input.split("\n\n")
    lines = map(parse_line, lines)

    return list(lines)


def read_input(filename):
    with open(filename) as file:
        content = file.read()

    return parse_input(content)


def has_passport_all_fields(passport):
    for field in PASSPORT_FIELDS.keys():
        if field not in passport:
            return False

    return True


def count_passports_with_all_fields(passports):
    count = 0

    for passport in passports:
        if has_passport_all_fields(passport):
            count += 1

    return count


def is_passport_valid(passport):
    for field, checker in PASSPORT_FIELDS.items():
        if field not in passport or not checker(passport[field]):
            return False

    return True


def count_valid_passports(passports):
    count = 0

    for passport in passports:
        if is_passport_valid(passport):
            count += 1

    return count


if __name__ == "__main__":
    passports = read_input('input.txt')

    first = count_passports_with_all_fields(passports)
    print(first)

    second = count_valid_passports(passports)
    print(second)
