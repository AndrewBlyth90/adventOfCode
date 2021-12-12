import unittest

import numpy as np

import dec11

mock_data = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526'
]

for y, line in enumerate(mock_data):
    for x, c in enumerate(line):
        mock_data[x, y] = int(c)





class dec11_test(unittest.TestCase):
    def test_first_problem(self):
        self.assertEqual(dec11.first_problem(mock_data), 1656)


if __name__ == '__main__':
    unittest.main()
