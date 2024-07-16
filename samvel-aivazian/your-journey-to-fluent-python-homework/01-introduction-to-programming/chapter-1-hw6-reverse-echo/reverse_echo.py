# reverse_echo.py

import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)


class ReverseEcho:
    """
    A class to capture and reverse echo lines of text.
    """

    def __init__(self):
        """
        Initializes the ReverseEcho object with an empty list to store lines of text.
        """
        self.lines = []

    def capture_lines(self, num_lines=3):
        """
        Captures lines of text from the user.

        Parameters:
        num_lines (int): Number of lines to capture from the user. Default is 3.
        """
        logging.info("Starting to capture lines.")
        for _ in range(num_lines):
            line = input("Enter a line of text: ")
            self.lines.append(line)
            logging.info(f"Captured line: {line}")

    def reverse_echo(self):
        """
        Prints the captured lines in reverse order.
        """
        logging.info("Echoing lines in reverse order.")
        for line in reversed(self.lines):
            print(line)
            logging.info(f"Echoed line: {line}")
