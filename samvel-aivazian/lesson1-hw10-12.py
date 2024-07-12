# Assignment 1: Cube Measurements
from typing import Tuple, Any


def cube_measurements(edge_length: int) -> tuple[int | Any, int | Any]:
    volume = edge_length ** 3
    surface_area = 6 * (edge_length ** 2)
    return volume, surface_area


# Assignment 2: Computer Set Cost Calculator
def total_cost_of_computer_sets(monitor_cost: int, system_unit_cost: int, keyboard_cost: int, mouse_cost: int) -> int:
    total_cost = 3 * (monitor_cost + system_unit_cost + keyboard_cost + mouse_cost)
    return total_cost


# Assignment 3: Basic Arithmetic Operations
def arithmetic_operations(num1: int, num2: int) -> tuple[int, int, int]:
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    return sum_result, difference, product


# For Assignment 1
edge_length_input = 5
volume_output, surface_area_output = cube_measurements(edge_length_input)
print(f"Volume: {volume_output}, Surface Area: {surface_area_output}")

# For Assignment 2
monitor_cost_input = 300
system_unit_cost_input = 400
keyboard_cost_input = 50
mouse_cost_input = 25
total_cost_output = total_cost_of_computer_sets(monitor_cost_input, system_unit_cost_input, keyboard_cost_input,
                                                mouse_cost_input)
print(f"Total Cost of Computer Sets: {total_cost_output}")

# For Assignment 3
num1_input = 10
num2_input = 5
sum_result, difference, product = arithmetic_operations(num1_input, num2_input)
print(f"Sum: {sum_result}, Difference: {difference}, Product: {product}")
