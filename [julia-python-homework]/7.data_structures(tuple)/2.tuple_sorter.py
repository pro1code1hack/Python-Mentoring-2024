"""Develop a program to sort elements of multiple tuples based on user preference 
(ascending or descending order)."""

# Input: Enter elements of the tuple: 5, 1, 9, 3
# Sort order (asc/desc): asc
# Output: Sorted Tuple: (1, 3, 5, 9)

elements = input("Enter elements of the tuple separted by commas: ")
sort_order = input("Sort order (asc/desc): ")
elements_list = [int(char) for char in elements.split(",")]

if sort_order == "asc":
    elements_list.sort()
elif sort_order == "desc":
    elements_list.sort(reverse=True)

sorted_tuple = tuple(elements_list)
print("Sorted Tuple: ", sorted_tuple)
