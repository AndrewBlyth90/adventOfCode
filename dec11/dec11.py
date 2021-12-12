from __future__ import annotations
from aocd import get_data
from typing import Generator


def format_data():
    coords = {}
    input_data = get_data(day=11, year=2021)
    input_data = input_data.split('\n')
    for y, line in enumerate(input_data):
        for x, c in enumerate(line):
            coords[x, y] = int(c)
    return coords


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    for x_d in (-1, 0, 1):
        for y_d in (-1, 0, 1):
            if x_d == y_d == 0:
                continue
            yield x + x_d, y + y_d


def second_problem(data):
    step = 0
    while True:
        step += 1
        todo = []

        for i, element in data.items():
            data[i] += 1
            if data[i] > 9:
                todo.append(i)

        while todo:
            point = todo.pop()
            if data[point] == 0:
                continue
            data[point] = 0

            for other in adjacent(*point):
                if other in data and data[other] != 0:
                    data[other] += 1
                    if data[other] > 9:
                        todo.append(other)
        if all(val == 0 for val in data.values()):
            break

    return step


def first_problem(data):
    flashes = 0
    for _ in range (100):
        todo = []

        for i, element in data.items():
            data[i] += 1
            if data[i] > 9:
                todo.append(i)

        while todo:
            point = todo.pop()
            if data[point] == 0:
                continue
            data[point] = 0
            flashes += 1

            for other in adjacent(*point):
                if other in data and data[other] != 0:
                    data[other] += 1
                    if data[other] > 9:
                        todo.append(other)
    return flashes

if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data))
    print('The answer to the first problem is: ', second_problem(data))