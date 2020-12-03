#!/usr/bin/env python

def parse_line(line):
    details, password = line.split(": ")
    numbers, char = details.split(" ")
    first, second = numbers.split("-")

    return {
        'text': password,
        'char': char,
        'first': int(first),
        'second': int(second)
    }


def parse_input(input):
    lines = input.split("\n")
    lines = map(parse_line, [line for line in lines])

    return [line for line in lines]


def read_input(filename):
    with open(filename) as file:
        content = file.read()

    return parse_input(content)


def min_max_valid_passwords(passwords):
    count = 0

    for password in passwords:
        occurrences = password['text'].count(password['char'])

        if occurrences >= password['first'] and occurrences <= password['second']:
            count += 1
    
    return count


def first_second_password_valid(passwords):
    count = 0

    for password in passwords:
        first = (password['text'][password['first'] - 1] == password['char'])
        second = (password['text'][password['second'] - 1] == password['char'])

        if first != second:
            count += 1

    return count


if __name__ == "__main__":
    passwords = read_input('input.txt')

    first = min_max_valid_passwords(passwords)
    print(first)

    second = first_second_password_valid(passwords)
    print(second)
