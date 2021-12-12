import unittest
import dec12

mock_data = {
    'fs': ['end', 'he', 'DX', 'pj'],
    'end': ['fs'],
    'he': ['DX', 'fs', 'pj', 'RW', 'zg'],
    'DX': ['he', 'start', 'pj', 'fs'],
    'start': ['DX', 'DX', 'pj', 'RW'],
    'pj': ['DX', 'DX', 'zg', 'he', 'RW', 'start', 'fs'],
    'zg': ['end', 'pj', 'RW', 'he'], 'sl': ['zg'],
    'RW': ['he', 'he', 'pj', 'zg', 'start'],
    'WI': ['he']
}


class dec12_test(unittest.TestCase):
    def test_first_problem(self):
        self.assertEqual(dec12.first_problem(mock_data, 'start', set()), 1656)


if __name__ == '__main__':
    unittest.main()
