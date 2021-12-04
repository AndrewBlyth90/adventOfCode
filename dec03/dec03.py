from aocd import get_data


def format_data():
    input_data = get_data(day=3, year=2021)
    input_data = input_data.split('\n')
    return input_data


def calculate_gamma(list):
    gamma_value = []
    for column in list:
        gamma_value.append(max(column, key=column.count))
    return ''.join(map(str, gamma_value))


def calculate_epsilon(list):
    epsilon_value = []
    for digit in list:
        if digit == '0':
            epsilon_value.append('1')
        if digit == '1':
            epsilon_value.append('0')
    return ''.join(map(str, epsilon_value))


def first_problem(data):
    transposed_list = list(map(list, zip(*data)))
    gamma = calculate_gamma(transposed_list)
    epsilon = calculate_epsilon(gamma)
    return int(gamma, 2) * int(epsilon, 2)

if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data))