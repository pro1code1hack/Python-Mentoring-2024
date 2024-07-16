# test_simple_interest_calculator.py

import unittest

from simple_interest_calculator import SimpleInterestCalculator


class TestSimpleInterestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleInterestCalculator()

    def test_calculate_interest(self):
        self.assertAlmostEqual(self.calculator.calculate_interest(1000, 5, 3), 150.0)
        self.assertAlmostEqual(self.calculator.calculate_interest(2000, 7.5, 5), 750.0)
        self.assertAlmostEqual(self.calculator.calculate_interest(1500, 4.3, 2), 129.0)


if __name__ == "__main__":
    unittest.main()
