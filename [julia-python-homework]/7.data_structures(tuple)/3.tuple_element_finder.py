"""Create a program that finds specific elements within a tuple based on user queries."""

# Input: Tuple: (1, 2, 3, 4, 5, 6)
# Enter element to search: 4
# Output: Element 4 found at index: 3

elements = input("Enter elements of the tuple separted by commas: ")
elements_tuple = tuple(int(char) for char in elements.split(","))
search_element = int(input("Enter element to search: "))
search_index = elements_tuple.index(search_element)
print(f"Element {search_element} found at index: {search_index}")
