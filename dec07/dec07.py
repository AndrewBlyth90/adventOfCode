import statistics

from aocd import get_data


def format_data():
    input_data = get_data(day=7, year=2021)
    input_data = input_data.split(',')
    input_data = list(map(int, input_data))
    return input_data


def first_problem(data):
    total = []
    for position in range(max(data)):
        temp = []
        for crab in data:
            temp.append(abs(crab - position))
        total.append(sum(temp))
    return min(total)

if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data))
    # print('The answer to the first problem is: ', fish_breeding(data, 256))