# test_temperature_converter.py

import unittest

from temperature_converter import TemperatureConverter


class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TemperatureConverter()

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(98.6), 37.0, places=1)


if __name__ == "__main__":
    unittest.main()
