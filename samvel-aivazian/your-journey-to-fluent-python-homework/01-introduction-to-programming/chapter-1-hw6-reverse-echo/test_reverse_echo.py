# test_reverse_echo.py

import sys
import unittest
from io import StringIO

from reverse_echo import ReverseEcho


class TestReverseEcho(unittest.TestCase):
    def setUp(self):
        self.reverser = ReverseEcho()

    def test_capture_and_reverse_echo(self):
        input_lines = ["First line", "Second line", "Third line"]
        expected_output = (
                "Enter a line of text: Enter a line of text: Enter a line of text: "
                + "\n".join(reversed(input_lines)) + "\n"
        )

        # Redirect stdin to simulate user input
        sys.stdin = StringIO("\n".join(input_lines) + "\n")

        # Redirect stdout to capture print statements
        sys.stdout = StringIO()

        self.reverser.capture_lines()
        self.reverser.reverse_echo()

        # Get the output and reset stdout
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
