# test_repeat_after_me.py

import sys
import unittest
from io import StringIO

from repeat_after_me import RepeatAfterMe


class TestRepeatAfterMe(unittest.TestCase):
    def setUp(self):
        self.repeater = RepeatAfterMe()

    def test_capture_and_repeat_lines(self):
        input_lines = ["First line", "Second line", "Third line"]
        # Include the expected prompts in the expected output
        expected_output = (
                "Enter a line of text: Enter a line of text: Enter a line of text: "
                + "\n".join(input_lines) + "\n"
        )

        # Redirect stdin to simulate user input
        sys.stdin = StringIO("\n".join(input_lines) + "\n")

        # Redirect stdout to capture print statements
        sys.stdout = StringIO()

        self.repeater.capture_lines()
        self.repeater.repeat_lines()

        # Get the output and reset stdout
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
