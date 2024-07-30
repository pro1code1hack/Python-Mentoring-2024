"""
Task 1: Tuple Analyzer
Objective: Write a program that allows the user to input a sequence of numbers, store them in a tuple, and analyze the tuple to provide insights.

Input: Enter numbers separated by commas: 1, 2, 3, 4, 5
Output: Tuple: (1, 2, 3, 4, 5)
        Sum: 15
        Average: 3
        Maximum: 5
        Minimum: 1
"""

def tuple_analyzer():
    input_numbers = input("Enter numbers separated by commas: ").strip()
    numbers_tuple = tuple(map(int, input_numbers.split(',')))
    
    tuple_sum = sum(numbers_tuple)
    tuple_average = tuple_sum / len(numbers_tuple)
    tuple_max = max(numbers_tuple)
    tuple_min = min(numbers_tuple)
    
    print(f"Tuple: {numbers_tuple}")
    print(f"Sum: {tuple_sum}")
    print(f"Average: {tuple_average}")
    print(f"Maximum: {tuple_max}")
    print(f"Minimum: {tuple_min}")

"""
Tuple Sorter
Objective: Develop a program to sort elements of multiple tuples based on user preference (ascending or descending order).

Input: Enter elements of the tuple: 5, 1, 9, 3
       Sort order (asc/desc): asc
Output: Sorted Tuple: (1, 3, 5, 9)
"""
def tuple_sorter():
    elements_str = input("Enter elements of the tuple separated by commas: ").strip()
    elements_list = elements_str.split(',')
    user_tuple = tuple(map(int, elements_list))
    
    sort_order = input("Sort order (asc/desc): ").strip().lower()
    
    if sort_order == 'asc':
        sorted_tuple = tuple(sorted(user_tuple))
    elif sort_order == 'desc':
        sorted_tuple = tuple(sorted(user_tuple, reverse=True))
    else:
        print("Invalid sort order. Please enter 'asc' or 'desc'.")
        return

    print(f"Sorted Tuple: {sorted_tuple}")


"""
Tuple Element Finder
Objective: Create a program that finds specific elements within a tuple based on user queries.

Input: Tuple: (1, 2, 3, 4, 5, 6)
       Enter element to search: 4
Output: Element 4 found at index: 3
"""
def tuple_element_finder():
    user_tuple_str = input("Tuple: ").strip()
    user_tuple = tuple(map(int, user_tuple_str[1:-1].split(','))) 
    element_to_search = int(input("Enter element to search: ").strip())

    try:
        index = user_tuple.index(element_to_search)
        print(f"Element {element_to_search} found at index: {index}")
    except ValueError:
        print(f"Element {element_to_search} not found in the tuple.")


"""
Task 4: Enumerate Sports Teams
Objective: Use the enumerate() function to list sports teams and their ranking based on user input.

Input: Enter teams (separated by commas): Lakers, Bulls, Celtics
Output: Team Rankings:
       1. Lakers
       2. Bulls
       3. Celtics
"""
def enumerate_sports_teams():
    teams_input = input("Enter teams (separated by commas): ").strip()
    teams_list = teams_input.split(',')
    
    print("Team Rankings:")
    for rank, team in enumerate(teams_list, start=1):
        print(f"{rank}.{team.strip()}")

enumerate_sports_teams()
