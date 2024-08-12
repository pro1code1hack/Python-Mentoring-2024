"""

### Task 1: The Guessing Game
**Objective:**: Write a program that selects a random number and asks the user to guess it. Use a while loop to allow multiple attempts until they guess correctly or choose to exit.
Input:
Guess the number: 8
Wrong! Try again or type 'exit' to stop: 5
Wrong! Try again or type 'exit' to stop: exit
Output:
The correct number was 7. Better luck next time!
"""


def display_menu():
    print("Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Modify an item")
    print("4. Exit")


def main():
    items = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            item_to_add = input("Enter the item to add: ")
            items.append(item_to_add)
            print(f"List: {items}")

        elif choice == '2':
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in items:
                items.remove(item_to_remove)
            print(f"List: {items}")

        elif choice == '3':
            item_to_modify = input("Enter the item to modify: ")
            if item_to_modify in items:
                new_item = input("Enter the new item: ")
                index = items.index(item_to_modify)
                items[index] = new_item
            print(f"List: {items}")

        elif choice == '4':
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()





