import unittest
import dec02

class MyTestCase(unittest.TestCase):
    def testFunctionOne(self):
        mockData = ['forward 1', 'forward 2', 'down 3', 'up 1']
        self.assertEqual(dec02.firstProblem(mockData), 6)
    def testFunctionTwo(self):
        mockData = ['down 4', 'up 2', 'forward 5']
        self.assertEqual(dec02.secondProblem(mockData), 50)


if __name__ == '__main__':
    unittest.main()
