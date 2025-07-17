import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self): # will run when we run our tests
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.compute("3*5")
        self.assertEqual(result, 12)

    def test_edge(self):
        result = self.calculator.compute("weffrfev")
        self.assertWarns(result)


if __name__ == '__main__':
    unittest.main()