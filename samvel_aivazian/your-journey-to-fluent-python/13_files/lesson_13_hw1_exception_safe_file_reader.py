import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def safe_file_reader(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            logging.info(f"File content:\n{content}")
    except FileNotFoundError:
        logging.info(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        logging.info(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    safe_file_reader('example.txt')
