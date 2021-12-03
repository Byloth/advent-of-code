#!/usr/bin/env python


def mul(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


def parse_line(line):
    command, value = line.split(" ")

    return command, int(value)


def parse_content(content):
    lines = content.split("\n")
    lines = map(parse_line, lines)
    
    return list(lines)


def read_file(filename):
    with open(filename) as file:
        content = file.read()

    return parse_content(content)


def navigate_simple(course):
    position = 0
    depth = 0

    for command, value in course:
        if command == "forward":
            position += value

        elif command == "down":
            depth += value

        elif command == "up":
            depth -= value

    return position, depth


def navigate_aim(course):
    position = 0
    depth = 0
    aim = 0

    for command, value in course:
        if command == "forward":
            position += value
            depth += aim * value

        elif command == "down":
            aim += value

        elif command == "up":
            aim -= value

    return position, depth


def main():
    course = read_file('input.txt')
    simple_coordinates = navigate_simple(course)
    first = mul(simple_coordinates)

    print(first)

    aim_coordinates = navigate_aim(course)
    second = mul(aim_coordinates)

    print(second)


if __name__ == "__main__":
    main()
