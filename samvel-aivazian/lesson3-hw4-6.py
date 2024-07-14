def average_of_evens() -> tuple[list[int], float]:
    """
    Calculate the average of even numbers within a specified range.

    Returns:
    tuple[list[int], float]: A tuple containing a list of even numbers and their average.
    """
    # Assuming the input range to be from 1 to 10 for demonstration purposes
    evens = [num for num in range(1, 11) if num % 2 == 0]
    average = sum(evens) / len(evens)
    return evens, average


def list_operations() -> dict[str, float | int | tuple | str | list[int]]:
    """
    Perform various operations on a predefined list of numbers.

    Returns:
    dict: A dictionary containing the results of the operations.
    """
    numbers = (3, 12, 5, 8, 4, 9, 15, 22, 10)
    operations_output = {
        "length": len(numbers),
        "sum": sum(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "average": sum(numbers) / len(numbers),
        "last": numbers[-1],
        "without_first_last": numbers[1:-1],
        "contains_4_and_9": "YES" if {4, 9}.issubset(numbers) else "NO",
        "third_from_end": numbers[-3],
        "replace_10_with_20": [20 if num == 10 else num for num in numbers]
    }
    return operations_output


def ascii_alphabet() -> list[str]:
    """
    Generate a list of the ASCII lowercase alphabet.

    Returns:
    list[str]: A list containing the ASCII lowercase alphabet.
    """
    alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return alphabet_list


if __name__ == "__main__":
    # Execute Task 4
    evens, average = average_of_evens()
    print(f"Evens: {evens}, Average of evens: {average}")

    # Execute Task 5
    list_ops = list_operations()
    print(list_ops)

    # Execute Task 6
    alphabet = ascii_alphabet()
    print(alphabet)
