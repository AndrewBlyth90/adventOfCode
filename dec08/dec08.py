from aocd import get_data


def format_data():
    input_data = get_data(day=8, year=2021)
    input_data = input_data.split('\n')
    segments = []
    for each in input_data:
        segments.append(each.split('| ')[1])
    return segments


def first_problem(data):
    total = 0
    for segment in data:
        digit = str(segment).split(' ')
        for num in digit:
            if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
                total += 1
    return total

if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data))
    # print('The answer to the first problem is: ', fish_breeding(data, 256))