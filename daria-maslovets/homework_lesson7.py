"""
### Task 1: Tuple Analyzer
**Objective:** Write a program that allows the user to `input` a sequence of numbers, store them in a `tuple`, and analyze the `tuple` to provide _insights_.
```python
Input: Enter numbers separated by commas: 1, 2, 3, 4, 5
Output: Tuple: (1, 2, 3, 4, 5)
        Sum: 15
        Average: 3
        Maximum: 5
        Minimum: 1
```
"""




from statistics import mean

user_input = input("Enter numbers separated by commas: ")
numbers = tuple(map(int, user_input.split(',')))

total_sum = sum(numbers)
average = mean(numbers)
maximum = max(numbers)
minimum = min(numbers)

print(f"Tuple: {numbers}")
print(f"Sum: {total_sum}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")








