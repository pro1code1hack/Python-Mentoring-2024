# temperature_converter.py

import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)


class TemperatureConverter:
    """
    A class to convert temperatures.
    """

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """
        Converts Fahrenheit to Celsius.

        Parameters:
        fahrenheit (float): Temperature in Fahrenheit

        Returns:
        float: Temperature in Celsius
        """
        logging.info(f"Converting {fahrenheit} Fahrenheit to Celsius.")
        return (fahrenheit - 32) * 5 / 9
