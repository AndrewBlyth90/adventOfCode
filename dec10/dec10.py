from aocd import get_data


def format_data():
        input_data = get_data(day=10, year=2021)
        input_data = input_data.split('\n')
        return input_data


def check_char(char):
    match char:
        case ')':
            return '('
        case '}':
            return '{'
        case '>':
            return '<'
        case ']':
            return '['
    return False


def get_value(char):
    match char:
        case ')':
            return 3
        case '}':
            return 1197
        case '>':
            return 25137
        case ']':
            return 57
    return 0


def first_problem(data):
    total = 0
    closing_tags = ')]}>'
    for string in data:
        current_opening_tag = []
        for char in string:
            if char in closing_tags:
                matching_tag = check_char(char)
                if matching_tag == current_opening_tag[-1]:
                    current_opening_tag.pop()
                    continue
                total += get_value(char)
                break
            current_opening_tag.append(char)
    return total


if __name__ == '__main__':
    data = format_data()
    print('The answer to the first problem is: ', first_problem(data))
