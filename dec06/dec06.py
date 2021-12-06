from aocd import get_data


def format_data():
    input_data = get_data(day=6, year=2021)
    input_data = input_data.split(',')
    input_data = list(map(int, input_data))
    return input_data


mock_data = [3, 4, 3, 1, 2]


def first_problem(data, depth):
    temp_array = data.copy()
    if depth > 0:
        for index, number in enumerate(data):
            if number == 0:
                temp_array[index] = 6
                temp_array.append(8)
            else:
                temp_array[index] = number - 1
        depth = depth - 1
        first_problem(temp_array, depth)
    return temp_array

if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data, 80))