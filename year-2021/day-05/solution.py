#!/usr/bin/env python


def smart_range(num1, num2):
    return range(min(num1, num2), max(num1, num2))


def parse_content(content):
    rows = content.split("\n")

    vents_coords = []
    for row in rows:
        xy1, xy2 = row.split(" -> ")
        x1, y1 = xy1.split(",")
        x2, y2 = xy2.split(",")

        vents_coords.append(((int(x1), int(y1)), (int(x2), int(y2))))

    return vents_coords


def read_file(filename):
    with open(filename) as file:
        content = file.read()

    return parse_content(content)


def generate_new_vents_map(x, y):
    return [[0] * x for _ in range(y)]


def draw_vents_on_map(vents_map, vents_coords):
    for vent_coords in vents_coords:
        x1, y1 = vent_coords[0]
        x2, y2 = vent_coords[1]

        if x1 == x2 or y1 == y2:
            #
            # TODO! 😉
            #
            # ... smart_range(...)
            #


def main():
    vents_coords = read_file('input.txt')
    vents_map = generate_new_vents_map(1000, 1000)


if __name__ == "__main__":
    main()
