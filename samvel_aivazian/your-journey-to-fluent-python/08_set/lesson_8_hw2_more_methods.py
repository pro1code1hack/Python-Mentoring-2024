import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def main():
    X = {1, 2, 3, 4, 5, 6, 7}
    Y = {5, 6, 7, 8, 9, 10}
    K = {7, 8, 9, 10, 11, 12}

    logging.info(f"Set X: {X}")
    logging.info(f"Set Y: {Y}")
    logging.info(f"Set K: {K}")

    X.intersection_update(Y, K)
    logging.info(f"Set X after intersection update with Y and K: {X}")

    Y.symmetric_difference_update(K)
    logging.info(f"Set Y after symmetric difference update with K: {Y}")

    is_X_subset_Y = X.issubset(Y)
    is_X_subset_K = X.issubset(K)
    logging.info(f"Is X a subset of Y? {is_X_subset_Y}")
    logging.info(f"Is X a subset of K? {is_X_subset_K}")

    K = frozenset(K)
    logging.info(f"Set K after converting to immutable: {K}")
    try:
        K.add(13)
    except AttributeError as e:
        logging.info(f"Error when trying to add to immutable set K: {e}")


if __name__ == "__main__":
    main()
