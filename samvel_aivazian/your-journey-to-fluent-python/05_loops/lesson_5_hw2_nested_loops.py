import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def nested_loops():
    for i in range(1, 6):
        logging.info(str(i) * i)


if __name__ == "__main__":
    nested_loops()
