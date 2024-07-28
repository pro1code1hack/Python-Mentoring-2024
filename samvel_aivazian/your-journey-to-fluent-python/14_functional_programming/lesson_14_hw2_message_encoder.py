import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


def reverse(text):
    return text[::-1]


def encode_characters(text):
    return ''.join(chr(ord(char) + 1) for char in text)


def compose(*functions):
    def composed_func(input):
        for func in functions:
            input = func(input)
        return input

    return composed_func


@execution_time_decorator
def encode_message(message):
    encoder = compose(reverse, encode_characters)
    return encoder(message)


if __name__ == "__main__":
    encoded_message = encode_message("hello world")
    logging.info(f"Encoded message: {encoded_message}")
