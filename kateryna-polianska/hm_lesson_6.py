"""
Task 1: List Manipulator

Write a program that allows the user to manipulate a list in various ways. The user can choose to add, remove, or modify items in the list.

Input:
Menu:

Add an item
Remove an item
Modify an item
View list
Exit
Choose an option: 1
Enter the item to add: Apple
Output:
List: ['Apple']
"""

def display_menu():
    print("\nMenu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Modify an item")
    print("4. View list")
    print("5. Exit")

def add_item(lst):
    item = input("Enter the item to add: ")
    lst.append(item)
    print(f"List: {lst}")

def remove_item(lst):
    item = input("Enter the item to remove: ")
    if item in lst:
        lst.remove(item)
        print(f"List: {lst}")
    else:
        print(f"Item '{item}' not found in the list.")

def modify_item(lst):
    old_item = input("Enter the item to modify: ")
    if old_item in lst:
        new_item = input("Enter the new item: ")
        index = lst.index(old_item)
        lst[index] = new_item
        print(f"List: {lst}")
    else:
        print(f"Item '{old_item}' not found in the list.")

def view_list(lst):
    print(f"List: {lst}")

def main():
    lst = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_item(lst)
        elif choice == '2':
            remove_item(lst)
        elif choice == '3':
            modify_item(lst)
        elif choice == '4':
            view_list(lst)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""
Task 2: List Slicer

Develop a program that allows users to input a list and then perform various slicing operations based on the user input.

"""

def get_list_from_user():
    user_input = input("Enter a list of numbers (separated by space): ")
    user_list = list(map(int, user_input.split()))
    return user_list

def get_slice_indices():
    start = int(input("Enter start index for slicing: "))
    stop = int(input("Enter stop index for slicing: "))
    return start, stop

def slice_list(lst, start, stop):
    return lst[start:stop]

def main():
    user_list = get_list_from_user()
    start, stop = get_slice_indices()
    sliced_list = slice_list(user_list, start, stop)
    print(f"The sliced list is: {sliced_list}")

if __name__ == "__main__":
    main()

"""
Task 3: Shopping List Organizer

Develop a program that helps users organize their shopping list by adding, viewing, removing, and sorting items alphabetically.

"""

def display_menu():
    print("\nMenu:")
    print("Choose an action (add/view/remove/exit): ", end='')

def add_item(lst):
    item = input("Enter an item to add: ")
    if isinstance(item, str):
        lst.append(item)
        lst.sort()
        print(f"Item added. Your current list is: {lst}")
    else:
        print("Sorry, it is not a string")

def view_list(lst):
    print(f"Shopping List: {lst}")

def remove_item(lst):
    item = input("Enter an item to remove: ")
    if item in lst:
        lst.remove(item)
        print(f"Item removed. Your current list is: {lst}")
    else:
        print(f"Item '{item}' not found in the list.")

def main():
    shopping_list = []
    while True:
        display_menu()
        action = input().strip().lower()
        if action == 'add':
            add_item(shopping_list)
        elif action == 'view':
            view_list(shopping_list)
        elif action == 'remove':
            remove_item(shopping_list)
        elif action == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""
Task 4: Average of Events

Generate a list of even elements using range from the input and display the average of them.
"""

def main():
    range_limit = int(input("Enter the range limit: "))
    
    # Generate the list of even numbers using list comprehension
    even_numbers = [num for num in range(1, range_limit + 1) if num % 2 == 0]
    
    # Calculate the average of the even numbers
    if even_numbers:
        average = sum(even_numbers) / len(even_numbers)
    else:
        average = 0
    
    # Display the results
    print(f"The even numbers are: {even_numbers}")
    print(f"The average of the even numbers is: {average}")

if __name__ == "__main__":
    main()

