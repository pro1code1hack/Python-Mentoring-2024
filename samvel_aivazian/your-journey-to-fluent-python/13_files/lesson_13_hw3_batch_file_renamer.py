import logging
import os

logging.basicConfig(level=logging.INFO, format='%(message)s')


def batch_rename(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        for filename in os.listdir(directory):
            old_file = os.path.join(directory, filename)
            if os.path.isfile(old_file):
                new_file = os.path.join(directory, f"{filename}_old")
                os.rename(old_file, new_file)
                logging.info(f"Renamed: '{filename}' to '{filename}_old'")
    except FileNotFoundError as e:
        logging.info(e)
    except Exception as e:
        logging.info(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    batch_rename('example_directory')
