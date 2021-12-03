import unittest
import dec03

class dec03_test(unittest.TestCase):
    def test_gamma(self):
        mock_data = ['1', '0', '0', '1', '1']
        self.assertEqual(dec03.calculate_gamma(mock_data), '10011')
    def test_epsilon(self):
        mock_data = ['1', '0', '0', '1', '1']
        self.assertEqual(dec03.calculate_epsilon(mock_data), '01100')
    def test_first_problem(self):
        mock_data = ['10', '11']
        self.assertEqual(dec03.first_problem(mock_data), 2)



if __name__ == '__main__':
    unittest.main()
