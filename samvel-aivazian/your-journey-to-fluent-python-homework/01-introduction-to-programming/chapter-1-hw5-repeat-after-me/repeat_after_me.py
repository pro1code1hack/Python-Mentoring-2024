# repeat_after_me.py

import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)


class RepeatAfterMe:
    """=
    A class to capture and repeat lines of text in the order they were entered.
    """

    def __init__(self):
        """
        Initializes the RepeatAfterMe object with an empty list to store lines of text.
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

    def repeat_lines(self):
        """
        Prints the captured lines in the order they were entered.
        """
        logging.info("Repeating lines in original order.")
        for line in self.lines:
            print(line)
            logging.info(f"Repeated line: {line}")
