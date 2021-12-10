from aocd import get_data


def format_data():
        input_data = get_data(day=9, year=2021)
        input_data = input_data.split('\n')
        data = []
        for line in input_data:
            input_data = [int(x) for x in line]
            data.append(input_data)
        return data


def get_value(data, x, y):
    if x < 0 or x >= len(data):
        return 10
    if y < 0 or y >= len(data[0]):
        return 10
    return data[x][y]


def first_problem(data):
    total = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            count = 0
            offsets = [[x+1, y], [x-1, y], [x, y-1], [x, y+1]]
            for offset in offsets:
                if data[x][y] < get_value(data, offset[0], offset[1]):
                    count += 1
            if count == 4:
                total += (1 + data[x][y])
    return total


if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data))