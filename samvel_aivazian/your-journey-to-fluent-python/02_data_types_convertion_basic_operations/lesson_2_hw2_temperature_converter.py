import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        logging.info(f"{fahrenheit} Fahrenheit is {celsius} Celsius")
        return celsius


def main():
    logging.info("Enter temperature in Fahrenheit: ")
    fahrenheit = float(input())
    TemperatureConverter.fahrenheit_to_celsius(fahrenheit)


if __name__ == "__main__":
    main()
