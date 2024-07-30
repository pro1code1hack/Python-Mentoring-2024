"""Develop a program that allows users to input a list and then 
perform various slicing operations based on the user input."""

# Input:
# Enter a list of numbers (separated by space): 10 20 30 40 50
# Enter start index for slicing: 1
# Enter stop index for slicing: 4
# Output:
# The sliced list is: [20, 30, 40]

str_of_numbers = input("Enter a list of numbers (separated by space): ")
start_index = int(input("Enter start index for slicing: "))
stop_index = int(input("Enter stop index for slicing: "))

list_of_str = str_of_numbers.split(" ")
list_of_nums = [int(char) for char in list_of_str]
output = list_of_nums[start_index:stop_index]

print("The sliced list is: ", output)
