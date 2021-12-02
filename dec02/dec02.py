from aocd import get_data

def getData():
    data = get_data(day=2, year=2021)
    data = data.split('\n')
    return data

def firstProblem(data):
    horizontal = 0
    vertical = 0
    for element in data:
        direction = element.split()[0]
        if direction == 'forward':
            horizontal = horizontal + int(element.split()[1])
        if direction == 'down':
            vertical = vertical + int(element.split()[1])
        if direction == 'up':
            vertical = vertical - int(element.split()[1])
    return horizontal * vertical
    print('The answer to the first problem is: ', horizontal * vertical)

def secondProblem(data):
    aim = 0
    vertical = 0
    horizontal = 0
    for element in data:
        direction = element.split()[0]
        if direction == 'down':
            aim = aim + int(element.split()[1])
        if direction == 'up':
            aim = aim - int(element.split()[1])
        if direction == 'forward':
            horizontal = horizontal + int(element.split()[1])
            vertical = vertical + (aim * int(element.split()[1]))
    return horizontal * vertical

if __name__ == '__main__':
    data = getData()
    print('The answer to the first problem is: ', firstProblem(data))
    print('The answer to the second problem is: ', secondProblem(data))
