import unittest
import dec06

mock_data = [3, 4, 3, 1, 2]

class dec05_test(unittest.TestCase):
    def test_first_problem(self):
        self.assertEqual(dec06.fish_breeding(mock_data, 80), 5934)
        self.assertEqual(dec06.fish_breeding(mock_data, 256), 26984457539)


if __name__ == '__main__':
    unittest.main()
