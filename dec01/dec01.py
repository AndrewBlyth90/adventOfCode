from aocd import get_data


def convertIntegers():
    data = get_data(day=1, year=2021)
    data = data.split()
    return [int(index) for index in data]


def calculateIncreases():
    increases = 0
    data = convertIntegers()
    for index, element in enumerate(data):
        if element > data[index - 1]:
            increases += 1
    print("The answer for part one of dec01 is: ", increases)


def slidingWindow():
    increaseArray = []
    increases = 0
    data = convertIntegers()
    for index, element in enumerate(data):
        if index < len(data)-2:
            sumOfThree = data[index] + data[index + 1] + data[index + 2]
            increaseArray.append(sumOfThree)
    for index, element in enumerate(increaseArray):
        if element > increaseArray[index - 1]:
            increases += 1


slidingWindow()
