import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def tuple_element_finder():
    logging.info("Enter elements of the tuple separated by commas: ")
    elements = tuple(map(int, input().split(',')))
    logging.info(f"Tuple: {elements}")

    logging.info("Enter element to search: ")
    element_to_search = int(input().strip())

    if element_to_search in elements:
        index = elements.index(element_to_search)
        logging.info(f"Element {element_to_search} found at index: {index}")
    else:
        logging.info(f"Element {element_to_search} not found in the tuple.")


if __name__ == "__main__":
    tuple_element_finder()
