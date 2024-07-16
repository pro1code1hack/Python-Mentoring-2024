# simple_interest_calculator.py

import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)


class SimpleInterestCalculator:
    """
    A class to calculate simple interest.
    """

    @staticmethod
    def calculate_interest(principal, rate, time):
        """
        Calculates simple interest.

        Parameters:
        principal (float): The principal amount
        rate (float): The rate of interest (as a percentage)
        time (float): The time period in years

        Returns:
        float: Calculated simple interest
        """
        logging.info(f"Calculating simple interest for principal {principal}, rate {rate}, time {time}.")
        return (principal * rate * time) / 100
