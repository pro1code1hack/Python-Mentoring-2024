import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def ascii_alphabet():
    alphabet = [chr(i) for i in range(97, 123)]
    logging.info(alphabet)


if __name__ == "__main__":
    ascii_alphabet()
