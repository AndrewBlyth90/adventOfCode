from aocd import get_data


def format_data():
    input_data = get_data(day=4, year=2021)
    input_data = input_data.splitlines()
    numbers = list(map(int, input_data[0].split(',')))
    boards = []
    for index in range(2, len(input_data), 6):
        board = []
        for number in range(5):
            board.append((list(map(int, input_data[index + number].split()))))
        boards.append(board)
    return numbers, boards


def check_row(row):
    for element in row:
        if(element != 'X'):
            return False
    return True


def check_board(board):
    for row in board:
        if check_row(row):
            return True
    for col in list(map(list, zip(*board))):
        if check_row(col):
            return True
    return False


def mark_board(board, number):
    for row in board:
        for index, element in enumerate(row):
            if number == element:
                row[index] = 'X'


def calculate_sum(board):
    total = 0
    for row in board:
        for element in row:
            if element != 'X':
                total = total + int(element)
    return total


def first_problem(numbers, boards):
    for number in numbers:
        for board in boards:
            mark_board(board, number)
            if check_board(board):
                return calculate_sum(board)*number

if __name__ == '__main__':
    numbers, boards = format_data()
    print('The answer to the first problem is: ', first_problem(numbers, boards))
