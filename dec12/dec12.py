from collections import defaultdict
from aocd import get_data


def format_data(data):
    graph = defaultdict(set)
    for row in data.split('\n'):
        p1, p2 = row.split('-')
        graph[p1].add(p2)
        graph[p2].add(p1)
    return graph


def first_problem(data, start, used):
    total = 0
    if start == 'end':
        return 1
    used = used.copy()
    used.add(start)
    for node in data[start]:
        if node.islower() and node in used:
            if node in ('start', 'end'):
                continue
        else:
            total += first_problem(data, node, used)
    return total


if __name__ == '__main__':
    data = format_data(get_data(day=12, year=2021))
    print('The answer to the first problem is: ', first_problem(data, 'start', set()))
