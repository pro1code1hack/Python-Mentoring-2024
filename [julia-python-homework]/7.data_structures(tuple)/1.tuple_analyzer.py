"""Write a program that allows the user to input a sequence of numbers, store them in 
a tuple, and analyze the tuple to provide insights."""

# Input: Enter numbers separated by commas: 1, 2, 3, 4, 5
# Output: Tuple: (1, 2, 3, 4, 5)
#  Sum: 15
#  Average: 3
#  Maximum: 5
#  Minimum: 1

my_input = input("Enter numbers separted by commas: ")
my_tuple = tuple(int(char) for char in my_input.split(","))
print("Tuple:", my_tuple)
print("Sum: ", sum(my_tuple))
print("Average: ", sum(my_tuple) // len(my_tuple))
print("Maximum: ", max(my_tuple))
print("Minimum: ", min(my_tuple))
