# main.py

import logging

from reverse_echo import ReverseEcho

# Setting up logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Program started.")
    reverser = ReverseEcho()
    reverser.capture_lines()
    reverser.reverse_echo()
    logging.info("Program ended.")
