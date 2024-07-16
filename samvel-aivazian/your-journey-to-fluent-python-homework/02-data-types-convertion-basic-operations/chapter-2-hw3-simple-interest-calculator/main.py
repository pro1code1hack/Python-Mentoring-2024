# main_simple_interest_calculator.py

import logging

from simple_interest_calculator import SimpleInterestCalculator

# Setting up logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Program started.")
    calculator = SimpleInterestCalculator()
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (as a percentage): "))
    time = float(input("Enter the time period in years: "))
    interest = calculator.calculate_interest(principal, rate, time)
    logging.info(f"Calculated simple interest: {interest}")
    print(f"The simple interest is {interest}")
    logging.info("Program ended.")
