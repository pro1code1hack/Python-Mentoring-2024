import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def convert_temperature(value, convert_to='F'):
    if convert_to == 'F':
        result = (value * 9 / 5) + 32
    elif convert_to == 'C':
        result = (value - 32) * 5 / 9
    else:
        logging.info("Invalid conversion direction.")
        return None
    return result


if __name__ == "__main__":
    logging.info(f"100 Celsius to Fahrenheit: {convert_temperature(100)}")
    logging.info(f"212 Fahrenheit to Celsius: {convert_temperature(212, 'C')}")  # Output: 100
