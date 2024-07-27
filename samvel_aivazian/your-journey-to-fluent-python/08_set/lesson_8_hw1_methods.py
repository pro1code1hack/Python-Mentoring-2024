import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def main():
    A = set(range(1, 11))
    B = set(range(5, 16))

    logging.info(f"Set A: {A}")
    logging.info(f"Set B: {B}")

    union = A | B
    logging.info(f"Union of A and B: {union}")

    intersection = A & B
    logging.info(f"Intersection of A and B: {intersection}")

    difference = A - B
    logging.info(f"Difference between A and B: {difference}")

    symmetric_difference = A ^ B
    logging.info(f"Symmetric difference between A and B: {symmetric_difference}")

    B.add(16)
    B.remove(5)
    logging.info(f"Set B after adding 16 and removing 5: {B}")

    is_A_subset_B = A.issubset(B)
    is_B_subset_A = B.issubset(A)
    logging.info(f"Is A a subset of B? {is_A_subset_B}")
    logging.info(f"Is B a subset of A? {is_B_subset_A}")


if __name__ == "__main__":
    main()
