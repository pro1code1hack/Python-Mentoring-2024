import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def tuple_sorter():
    logging.info("Enter elements of the tuple separated by commas: ")
    elements = tuple(map(int, input().split(',')))
    logging.info("Sort order (asc/desc): ")
    sort_order = input().strip().lower()

    if sort_order == 'asc':
        sorted_tuple = tuple(sorted(elements))
    elif sort_order == 'desc':
        sorted_tuple = tuple(sorted(elements, reverse=True))
    else:
        logging.info("Invalid sort order. Please enter 'asc' or 'desc'.")
        return

    logging.info(f"Sorted Tuple: {sorted_tuple}")


if __name__ == "__main__":
    tuple_sorter()
