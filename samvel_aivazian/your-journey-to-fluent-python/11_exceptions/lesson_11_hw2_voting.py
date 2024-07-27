import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def check_voter_age(age):
    try:
        if age < 18:
            raise ValueError("Error: You are too young to vote.")
        else:
            logging.info("You are allowed to vote.")
    except ValueError as e:
        logging.info(e)


if __name__ == "__main__":
    check_voter_age(21)
    check_voter_age(16)