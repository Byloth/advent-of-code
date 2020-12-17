#!/usr/bin/env python

MAX_DIFFERENCE = 3


def parse_content(content):
    lines = content.split("\n")
    lines = map(lambda line: int(line), lines)
    
    return list(lines)


def read_file(filename):
    with open(filename) as file:
        content = file.read()

    return parse_content(content)


def sort_and_add_last(adapters):
    adapters = sorted(adapters)
    last_value = adapters[-1]

    adapters.append(last_value + 3)

    return adapters


def sort_and_add_first_last(adapters):
    adapters = sort_and_add_last(adapters)

    return [0, *adapters]


def count_differences(adapters):
    adapters = sort_and_add_last(adapters)
    differences = [0] * MAX_DIFFERENCE

    jolts = 0

    for value in adapters:
        jump = value - jolts
        differences[jump - 1] += 1
        jolts += jump

    return (difference for difference in differences)


def count_arrangements(adapters):
    adapters = sort_and_add_first_last(adapters)
    length = len(adapters)

    routes = {}
    index = length - 1
    
    while index >= 0:
        count = 0
        value = adapters[index]

        increment = 1
        next_index = index + increment

        while next_index < length:
            next_value = adapters[next_index]

            if next_value > (value + MAX_DIFFERENCE):
                break

            count += routes[next_value]
            
            increment += 1
            next_index = index + increment

        index -= 1
        routes[value] = count if count else 1

    return routes[adapters[0]]


if __name__ == "__main__":
    adapters = read_file('input.txt')

    one, _, three = count_differences(adapters)
    print(one * three)

    second = count_arrangements(adapters)
    print(second)
