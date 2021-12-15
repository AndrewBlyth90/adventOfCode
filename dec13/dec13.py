from aocd import get_data

def format_data():
    points = set()
    input_data = get_data(day=13, year=2021)
    points_s, instructions = input_data.split('\n\n')
    for line in points_s.splitlines():
        x_s, y_s = line.split(',')
        points.add((int(x_s), int(y_s)))
    return points, instructions

def print_points(points: set[tuple[int, int]]) -> None:
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if(x, y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print()

def  first_problem(points, instructions):
    for line in instructions.splitlines():
        instructions_s, n_S = line.split('=')
        axis = instructions_s[-1]
        n = int(n_S)
        if axis == 'x':
            points = {
                (
                    x if x < n else n - (x - n),
                    y,
                )
                for x, y in points
            }
        elif axis == 'y':
            points = {
                (
                    x,
                    y if y < n else n - (y - n),
                )
                for x, y in points
            }
        else:
            raise AssertionError(f'unexpected axis: {axis}')
    print_points(points)
    return len(points)

if __name__ == '__main__':
    points, instructions = format_data()
    print('The answer to the first problem is: ', first_problem(points, instructions))
