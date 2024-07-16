# main.py

import logging

from temperature_converter import TemperatureConverter

# Setting up logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Program started.")
    converter = TemperatureConverter()
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = converter.fahrenheit_to_celsius(fahrenheit)
    logging.info(f"Converted {fahrenheit} Fahrenheit to {celsius} Celsius.")
    print(f"{fahrenheit} Fahrenheit is {celsius} Celsius")
    logging.info("Program ended.")
