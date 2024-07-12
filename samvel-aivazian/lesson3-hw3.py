# Task 3: Shopping List Organizer
# A program that helps users organize their shopping list with add, view, remove, and sort functionalities.
def shopping_list_organizer() -> None:
    shopping_list = []  # Initial empty shopping list

    def print_menu() -> None:
        print("\nMenu:")
        print("1. Add item")
        print("2. View list")
        print("3. Remove item")
        print("4. Exit")

    while True:
        print_menu()
        choice = input("Choose an action (add/view/remove/exit): ").lower()

        if choice == "add":
            # Add an item
            item_to_add = input("Enter an item to add: ")

            # Check if the item is a string
            if isinstance(item_to_add, str):
                shopping_list.append(item_to_add)
                shopping_list.sort()  # Sort the list alphabetically
                print(f"Item added. Your current list is: {shopping_list}")
            else:
                print("Sorry, it is not a string")

        elif choice == "view":
            # View the list
            print(f"Shopping List: {shopping_list}")

        elif choice == "remove":
            # Remove an item
            item_to_remove = input("Enter an item to remove: ")

            # Check if the item exists in the list
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"Item removed. Your current list is: {shopping_list}")
            else:
                print("Item not found in the list.")

        elif choice == "exit":
            # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


shopping_list_organizer()
