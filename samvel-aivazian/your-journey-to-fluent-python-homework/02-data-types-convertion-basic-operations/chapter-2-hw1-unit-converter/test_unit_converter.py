# test_unit_converter.py

import unittest

from unit_converter import UnitConverter


class TestUnitConverter(unittest.TestCase):
    def setUp(self):
        self.converter = UnitConverter()

    def test_inches_to_cm(self):
        self.assertAlmostEqual(self.converter.inches_to_cm(10), 25.4)
        self.assertAlmostEqual(self.converter.inches_to_cm(0), 0.0)
        self.assertAlmostEqual(self.converter.inches_to_cm(1), 2.54)


if __name__ == "__main__":
    unittest.main()
