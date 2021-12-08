import unittest
import dec07

mock_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


class dec07_test(unittest.TestCase):
    def test_first_problem(self):
        self.assertEqual(dec07.first_problem(mock_data), 37)

    def test_second_problem(self):
        self.assertEqual(dec07.second_problem(mock_data), 168)


if __name__ == '__main__':
    unittest.main()
