# unit_converter.py

import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)


class UnitConverter:
    """
    A class to convert units of measurement.
    """

    @staticmethod
    def inches_to_cm(inches):
        """
        Converts inches to centimeters.

        Parameters:
        inches (float): Length of inches

        Returns:
        float: Length in centimeters
        """
        logging.info(f"Converting {inches} inches to centimeters.")
        return inches * 2.54
