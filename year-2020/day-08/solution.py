#!/usr/bin/env python

def parse_line(line):
    instruction, argument = line.split(" ")

    return instruction, int(argument)


def parse_content(content: str):
    lines = content.split("\n")
    lines = map(parse_line, lines)

    return list(lines)


def read_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return parse_content(content)


def execute(program):
    # pylint: disable=invalid-name

    lines = []
    length = len(program)

    # LOL! x86 16bit naming convention! 😇
    #
    IP = 0
    AX = 0

    while IP < length:
        if IP in lines:
            break

        lines.append(IP)

        instruction, argument = program[IP]

        if instruction == "acc":
            AX += argument
            IP += 1

        elif instruction == "jmp":
            IP += argument

        elif instruction == "nop":
            IP += 1

    else:
        return AX, False

    return AX, IP


def next_eventually_broken_line(program, pointer):
    while program[pointer][0] == "acc":
        pointer += 1

    return pointer


def fix_corrupted_line(program, pointer):
    def fix():
        instruction, argument = program[pointer]

        if instruction == "jmp":
            program[pointer] = ("nop", argument)

        elif instruction == "nop":
            program[pointer] = ("jmp", argument)

    fix()

    return fix


def fix_and_execute(program):
    def revert():
        pass

    pointer = -1
    result = None
    error = True

    while error is not False:
        revert()

        pointer = next_eventually_broken_line(program, pointer + 1)
        revert = fix_corrupted_line(program, pointer)

        result, error = execute(program)

    return result


def main():
    program = read_file('./input.txt')

    first, _ = execute(program)
    print("Solution part 1:", first)

    second = fix_and_execute(program)
    print("Solution part 2:", second)


if __name__ == "__main__":
    main()
