import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class SimpleInterestCalculator:
    @staticmethod
    def calculate_simple_interest(principal, rate, time):
        interest = (principal * rate * time) / 100
        logging.info(f"Simple Interest is {interest}")
        return interest


def main():
    logging.info("Enter the principal amount: ")
    principal = float(input())
    logging.info("Enter the rate of interest: ")
    rate = float(input())
    logging.info("Enter the time period in years: ")
    time = float(input())
    SimpleInterestCalculator.calculate_simple_interest(principal, rate, time)


if __name__ == "__main__":
    main()
