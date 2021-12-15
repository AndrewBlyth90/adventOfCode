import collections
from aocd import get_data


def format_data():
    data = get_data(day=14, year=2021)
    rules = {}
    starting_template, rest = data.split('\n\n')
    for row in rest.splitlines():
        p1, p2 = row.split(' -> ')
        rules[p1] = p2
    return starting_template, rules


def first_problem(starting_template, rules):
    pair_counts = collections.Counter()
    for i in range(0, len(starting_template) - 1):
        pair_counts[starting_template[i:i + 2]] += 1
    for _ in range(10):
        new_counts = collections.Counter()
        char_counts = collections.Counter()
        for k, v in pair_counts.items():
            new_counts[f'{k[0]}{rules[k]}'] += v
            new_counts[f'{rules[k]}{k[1]}'] += v

            char_counts[k[0]] += v
            char_counts[rules[k]] += v

        pair_counts = new_counts

    char_counts[starting_template[-1]] += 1
    print(char_counts)





if __name__ == '__main__':
    starting_template, rules = format_data()
    print('The answer to the first problem is: ', first_problem(starting_template, rules))
