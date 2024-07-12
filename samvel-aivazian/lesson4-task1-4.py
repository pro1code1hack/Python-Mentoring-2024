# Task 1: Tuple Analyzer
from typing import Tuple, List


def tuple_analyzer(input_numbers: str) -> tuple:
    numbers_tuple = tuple(map(int, input_numbers.split(',')))
    sum_numbers = sum(numbers_tuple)
    average = sum_numbers / len(numbers_tuple)
    maximum = max(numbers_tuple)
    minimum = min(numbers_tuple)
    return numbers_tuple, sum_numbers, average, maximum, minimum


# Task 2: Tuple Sorter
def tuple_sorter(input_elements: str, order: str) -> tuple[int, ...]:
    elements = tuple(map(int, input_elements.split(',')))
    sorted_elements = tuple(sorted(elements, reverse=(order == 'desc')))
    return sorted_elements


# Task 3: Tuple Element Finder
def tuple_element_finder(input_tuple: tuple[int], element_to_search: int) -> int:
    index = input_tuple.index(element_to_search) if element_to_search in input_tuple else -1
    return index


# Task 4: Enumerate Sports Teams
def enumerate_sports_teams(input_teams: str) -> list[tuple[int, str]]:
    teams_list = input_teams.split(',')
    ranked_teams = enumerate(teams_list, start=1)
    return list(ranked_teams)


input_numbers = "1,2,3,4,5"
task_1_results = tuple_analyzer(input_numbers)
print(task_1_results)

input_elements = "5,1,9,3"
sort_order = "asc"
task_2_results = tuple_sorter(input_elements, sort_order)
print(task_2_results)

input_tuple = (1, 2, 3, 4, 5, 6)
element_to_search = 4
task_3_index = tuple_element_finder(input_tuple, element_to_search)
print(task_3_index)

input_teams = "Lakers,Bulls,Celtics"
task_4_rankings = enumerate_sports_teams(input_teams)
print(task_4_rankings)
