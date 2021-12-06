#!/usr/bin/env python


def parse_numbers(numbers):
    return [int(number) for number in numbers.split(",")]


def parse_boards(boards):
    result = []

    for board in boards:
        board = board.replace("  ", " ")
        lines = board.split("\n")
        
        rows = []
        for line in lines:
            row = line.strip()
            rows.append([[int(number), False] for number in row.split(" ")])

        result.append(rows)

    return result


def parse_content(content):
    rows = content.split("\n\n")

    numbers = parse_numbers(rows[0])
    boards = parse_boards(rows[1:])

    return numbers, boards


def read_file(filename):
    with open(filename) as file:
        content = file.read()

    return parse_content(content)


def check_board_row(board, y):
    return all(marked for _, marked in board[y])


def check_board_column(board, x):
    column = [row[x] for row in board]

    return all(marked for _, marked in column)


def check_board(board, x, y):
    return check_board_row(board, y) or check_board_column(board, x)


def mark_number(number, board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell[0] == number:
                cell[1] = True

                return check_board(board, x, y)


def get_first_winning_values(numbers, boards):
    for number in numbers:
        for board in boards:
            if mark_number(number, board):
                return number, board


def get_last_winning_values(numbers, boards):
    boards = boards.copy()

    for number in numbers:
        indexes_to_remove = []

        for index, board in enumerate(boards):
            if mark_number(number, board):
                indexes_to_remove.insert(0, index)
        
        for index in indexes_to_remove:
            if len(boards) > 1:
                del boards[index]

            else:
                return number, boards[index]
                

def sum_unmarked_cells(board):
    result = 0

    for row in board:
        for cell in row:
            if not cell[1]:
                result += cell[0]

    return result


def main():
    numbers, boards = read_file('input.txt')
    first_winning_number, first_winning_board = get_first_winning_values(numbers, boards)

    score = sum_unmarked_cells(first_winning_board)
    first = score * first_winning_number

    print(first)

    last_winning_number, last_winning_board = get_last_winning_values(numbers, boards)

    score = sum_unmarked_cells(last_winning_board)
    second = score * last_winning_number

    print(second)


if __name__ == "__main__":
    main()
