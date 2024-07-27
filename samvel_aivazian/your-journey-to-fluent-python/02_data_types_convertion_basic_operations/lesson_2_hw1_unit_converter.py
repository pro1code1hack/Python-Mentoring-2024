import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class UnitConverter:
    @staticmethod
    def inches_to_centimeters(inches):
        centimeters = inches * 2.54
        logging.info(f"{inches} inches is {centimeters} centimeters")
        return centimeters


def main():
    logging.info("Enter length in inches: ")
    inches = float(input())
    UnitConverter.inches_to_centimeters(inches)


if __name__ == "__main__":
    main()
