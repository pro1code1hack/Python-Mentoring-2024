from typing import Tuple, List


def tuple_analyzer(input_numbers: str) -> Tuple[Tuple[int, ...], int, float, int, int]:
    """
    Analyze a tuple of numbers to calculate the sum, average, maximum, and minimum.

    Args:
    input_numbers (str): A string of comma-separated numbers.

    Returns:
    Tuple[Tuple[int, ...], int, float, int, int]: A tuple containing the input numbers as a tuple,
                                                 the sum of the numbers, the average, the maximum,
                                                 and the minimum.
    """
    numbers_tuple = tuple(map(int, input_numbers.split(',')))
    sum_numbers = sum(numbers_tuple)
    average = sum_numbers / len(numbers_tuple)
    maximum = max(numbers_tuple)
    minimum = min(numbers_tuple)
    return numbers_tuple, sum_numbers, average, maximum, minimum


def tuple_sorter(input_elements: str, order: str) -> Tuple[int, ...]:
    """
    Sort a tuple of numbers in ascending or descending order.

    Args:
    input_elements (str): A string of comma-separated numbers.
    order (str): The order to sort the elements ('asc' for ascending, 'desc' for descending).

    Returns:
    Tuple[int, ...]: A tuple containing the sorted numbers.
    """
    elements = tuple(map(int, input_elements.split(',')))
    sorted_elements = tuple(sorted(elements, reverse=(order == 'desc')))
    return sorted_elements


def tuple_element_finder(input_tuple: Tuple[int, ...], element_to_search: int) -> int:
    """
    Find the index of an element in a tuple. If the element is not found, return -1.

    Args:
    input_tuple (Tuple[int, ...]): The tuple to search.
    element_to_search (int): The element to search for.

    Returns:
    int: The index of the element if found, otherwise -1.
    """
    return input_tuple.index(element_to_search) if element_to_search in input_tuple else -1


def enumerate_sports_teams(input_teams: str) -> List[Tuple[int, str]]:
    """
    Enumerate sports teams, assigning a rank starting from 1.

    Args:
    input_teams (str): A string of comma-separated team names.

    Returns:
    List[Tuple[int, str]]: A list of tuples where each tuple contains a rank and a team name.
    """
    teams_list = input_teams.split(',')
    ranked_teams = enumerate(teams_list, start=1)
    return list(ranked_teams)


if __name__ == "__main__":
    # Execute Task 1
    print("Task 1: Tuple Analyzer")
    input_numbers = "1,2,3,4,5"
    task_1_results = tuple_analyzer(input_numbers)
    print("Task 1 Results:", task_1_results)

    # Execute Task 2
    print("\nTask 2: Tuple Sorter")
    input_elements = "5,1,9,3"
    sort_order = "asc"
    task_2_results = tuple_sorter(input_elements, sort_order)
    print("Task 2 Results:", task_2_results)

    # Execute Task 3
    print("\nTask 3: Tuple Element Finder")
    input_tuple = (1, 2, 3, 4, 5, 6)
    element_to_search = 4
    task_3_index = tuple_element_finder(input_tuple, element_to_search)
    print("Task 3 Results:", task_3_index)

    # Execute Task 4
    print("\nTask 4: Enumerate Sports Teams")
    input_teams = "Lakers,Bulls,Celtics"
    task_4_rankings = enumerate_sports_teams(input_teams)
    print("Task 4 Results:", task_4_rankings)
