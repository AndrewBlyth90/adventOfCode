import unittest
import dec05

mock_data = ['0,9 -> 5,9',
             '8,0 -> 0,8',
             '9,4 -> 3,4',
             '2,2 -> 2,1',
             '7,0 -> 7,4',
             '6,4 -> 2,0',
             '0,9 -> 2,9',
             '3,4 -> 1,4',
             '0,0 -> 8,8',
             '5,5 -> 8,2']

class dec05_test(unittest.TestCase):
    def test_first_problem(self):
        self.assertEqual(dec05.first_problem(mock_data), 5)
        # self.assertEqual(dec05.second_problem(mock_data), 12)


if __name__ == '__main__':
    unittest.main()
