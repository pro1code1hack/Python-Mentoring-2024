"""
Task 1: Tuple Analyzer

Write a program that allows the user to `input` a sequence of numbers, store them in a `tuple`, and analyze the `tuple` to provide _insights_.

Input: Enter numbers separated by commas: 1, 2, 3, 4, 5
Output: Tuple: (1, 2, 3, 4, 5)
        Sum: 15
        Average: 3
        Maximum: 5
        Minimum: 1
"""

numbers = input("Enter numbers separated by commas: ")
num_tuple = tuple(map(int, numbers.split(',')))

sum_numbers = sum(num_tuple)
average = sum_numbers / len(num_tuple)
maximum = max(num_tuple)
minimum = min(num_tuple)

print(f"Tuple: {num_tuple}")
print(f"Sum: {sum_numbers}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")


"""
Task 2: Tuple Sorter

Develop a program to sort elements of multiple `tuples` based on user preference (`ascending` or `descending` order).


Input: Enter elements of the tuple: 5, 1, 9, 3
       Sort order (asc/desc): asc
Output: Sorted Tuple: (1, 3, 5, 9)

"""

elements = input("Enter elements of the tuple: ")
sort_order = input("Sort order (asc/desc): ")

tuple_elements = tuple(map(int, elements.split(',')))

if sort_order == 'asc':
    sorted_tuple = tuple(sorted(tuple_elements))
elif sort_order == 'desc':
    sorted_tuple = tuple(sorted(tuple_elements, reverse=True))
else:
    print("Invalid sort order")
    sorted_tuple = tuple_elements

print(f"Sorted Tuple: {sorted_tuple}")


"""
Task 3: Tuple Element Finder

Create a program that finds specific elements within a `tuple` based on user queries.

Input: Tuple: (1, 2, 3, 4, 5, 6)
       Enter element to search: 4
Output: Element 4 found at index: 3
"""

elements = input("Tuple: ")
tuple_elements = tuple(map(int, elements.split(',')))

element_to_search = int(input("Enter element to search: "))

if element_to_search in tuple_elements:
    index = tuple_elements.index(element_to_search)
    print(f"Element {element_to_search} found at index: {index}")
else:
    print(f"Element {element_to_search} not found in the tuple")


"""
Task 4: Enumerate Sports Teams

Use the `enumerate()` function to list sports teams and their ranking based on user `input`.

Input: Enter teams (separated by commas): Lakers, Bulls, Celtics
Output: Team Rankings:
       1. Lakers
       2. Bulls
       3. Celtics

"""

teams = input("Enter teams: ")
team_list = teams.split(',')

print("Team Rankings:")
for index, team in enumerate(team_list, start=1):
    print(f"{index}. {team.strip()}")

