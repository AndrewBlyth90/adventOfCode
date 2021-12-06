import copy

from aocd import get_data


def format_data():
    input_data = get_data(day=6, year=2021)
    input_data = input_data.split(',')
    input_data = list(map(int, input_data))
    return input_data


def fish_breeding(data, days):
    fish_number = []

    for num in range(9):
        counter = 0
        for fish in data:
            if fish == num:
                counter += 1
        fish_number.append(counter)

    for day in range(days):
        temp_array = fish_number.copy()
        for item in range(len(fish_number)):
            fish_number[item-1] = temp_array[item]
        fish_number[6] += temp_array[0]
    return sum(fish_number)


if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', fish_breeding(data, 80))
    print('The answer to the first problem is: ', fish_breeding(data, 256))