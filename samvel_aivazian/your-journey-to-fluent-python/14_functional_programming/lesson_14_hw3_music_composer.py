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


def add_notes(*notes):
    return list(notes)


def echo_effect(notes):
    return notes + notes[::-1]


def speed_change(notes, factor):
    return notes[::factor]


def compose(*functions):
    def composed_func(input):
        for func in functions:
            input = func(input)
        return input

    return composed_func


@execution_time_decorator
def compose_music(notes):
    music_composer = compose(echo_effect, lambda x: speed_change(x, 2))
    return music_composer(notes)


if __name__ == "__main__":
    notes = add_notes("C", "E", "G", "B")
    logging.info(f"Original notes: {notes}")
    composed_music = compose_music(notes)
    logging.info(f"Composed music with effects: {composed_music}")
