# main.py

import logging

from unit_converter import UnitConverter

# Setting up logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Program started.")
    converter = UnitConverter()
    inches = float(input("Enter length in inches: "))
    cm = converter.inches_to_cm(inches)
    logging.info(f"Converted {inches} inches to {cm} cm.")
    print(f"{inches} inches is {cm} cm")
    logging.info("Program ended.")
