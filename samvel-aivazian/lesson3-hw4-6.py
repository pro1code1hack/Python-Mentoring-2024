# Task 4: Average of Evens
def average_of_evens() -> list[int]:
    # Assuming the input range to be from 1 to 10 for demonstration purposes
    evens = [num for num in range(1, 11) if num % 2 == 0]
    average = sum(evens) / len(evens)
    return evens, average

# Task 5: List of numbers operations
def list_operations() -> dict[str]:
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

# Task 6: ASCII alphabet
def ascii_alphabet() -> list[str]:
    alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return alphabet_list


# Execute the tasks
evens, average = average_of_evens()
print(f"evens = {evens} and its average = {average}")

list_ops = list_operations()
print(list_ops)

alphabet = ascii_alphabet()
print(alphabet)