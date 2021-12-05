import itertools

from aocd import get_data
from collections import defaultdict


def format_data():
    input_data = get_data(day=5, year=2021)
    input_data = input_data.split('\n')
    return input_data



def first_problem(data):
    count = defaultdict(lambda: 0)
    for element in data:
        beginning, end = element.split('->')
        x1, y1 = [int(coord) for coord in beginning.split(',')]
        x2, y2 = [int(coord) for coord in end.split(',')]
        if x1 == x2:
            for num in range(min(y1, y2), max(y1, y2) + 1):
                count[(x1, num)] += 1
        if y1 == y2:
            for num in range(min(x1, x2), max(x1, x2) + 1):
                count[(num, y1)] += 1
    return len(list(filter((lambda num: num > 1), count.values())))

#
# def second_problem(data):
#     count = defaultdict(lambda: 0)
#     for element in data:
#         beginning, end = element.split('->')
#         x1, y1 = [int(coord) for coord in beginning.split(',')]
#         x2, y2 = [int(coord) for coord in end.split(',')]
#         for x, y in itertools.product(range((x1, x2) + 1), range(max(y1, y2) + 1)):
#             for x, y in zip(x, y):
#                 count[(x, y)] += 1
#     return len(list(filter((lambda num: num > 1), count.values())))


if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data))
    # print('The answer to the first problem is: ', second_problem(data))