# main.py

import logging

from repeat_after_me import RepeatAfterMe

# Setting up logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Program started.")
    repeater = RepeatAfterMe()
    repeater.capture_lines()
    repeater.repeat_lines()
    logging.info("Program ended.")
