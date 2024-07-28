import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class TextRepeater:
    def __init__(self):
        self.lines = []

    def capture_lines(self):
        for _ in range(3):
            logging.info("Enter a line of text: ")
            line = input()
            self.lines.append(line)

    def repeat_lines(self):
        logging.info("Repeating lines:")
        for line in self.lines:
            logging.info(line)


def main():
    text_repeater = TextRepeater()
    text_repeater.capture_lines()
    text_repeater.repeat_lines()


if __name__ == "__main__":
    main()
