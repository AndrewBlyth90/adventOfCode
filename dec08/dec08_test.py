import unittest
import dec08

mock_data = [
            'fdgacbe cefdb cefbgd gcbe',
             'fcgedb cgb dgebacf gc',
             'cg cg fdcagb cbg',
             'efabcd cedba gadfec cb',
             'gecf egdcabf bgf bfgea',
             'gebdcfa ecba ca fadegcb',
             'cefg dcbef fcge gbcadfe',
             'ed bcgafe cdgba cbgef',
             'gbdfcae bgc cg cgb',
             'fgae cfgab fg bagce'
            ]



class dec07_test(unittest.TestCase):
    def test_first_problem(self):
        self.assertEqual(dec08.first_problem(mock_data), 26)

if __name__ == '__main__':
    unittest.main()
