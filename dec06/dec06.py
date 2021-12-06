from aocd import get_data


def format_data():
    input_data = get_data(day=6, year=2021)
    input_data = input_data.split('\n')
    return input_data

def first_problem(data):
    print(data)


if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data))