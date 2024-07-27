import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def reverse_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in reversed(lines):
                file.write(line)

        logging.info(f"File content of '{file_path}' has been reversed.")
    except FileNotFoundError:
        logging.info(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        logging.info(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    reverse_file_content('example.txt')
