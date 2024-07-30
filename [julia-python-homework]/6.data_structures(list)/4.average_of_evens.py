"""Generate a list of even elements using range from 
the input and display the average of even of them"""

list_elements = input("Enter a list of numbers (separated by space): ")
list_numbers = [int(char) for char in list_elements.split(" ") if int(char) % 2 == 0]
avg = round(sum(list_numbers) / len(list_numbers))
print("The average of even numbers is:", avg)
