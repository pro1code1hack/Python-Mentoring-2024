def shopping_list_organizer() -> None:
    """
    A program that helps users organize their shopping list with add, view, remove, and exit functionalities.
    """
    shopping_list = []  # Initial empty shopping list

    def print_menu() -> None:
        """
        Print the menu options for the shopping list organizer.
        """
        print("\nMenu:")
        print("1. Add item")
        print("2. View list")
        print("3. Remove item")
        print("4. Exit")

    while True:
        print_menu()
        choice = input("Choose an action (add/view/remove/exit): ").strip().lower()

        if choice == "add":
            item_to_add = input("Enter an item to add: ").strip()

            if item_to_add:  # Ensure the item is not empty
                shopping_list.append(item_to_add)
                shopping_list.sort()  # Sort the list alphabetically
                print(f"Item added. Your current list is: {shopping_list}")
            else:
                print("Item cannot be empty.")

        elif choice == "view":
            print(f"Shopping List: {shopping_list}")

        elif choice == "remove":
            item_to_remove = input("Enter an item to remove: ").strip()

            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"Item removed. Your current list is: {shopping_list}")
            else:
                print("Item not found in the list.")

        elif choice == "exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    shopping_list_organizer()
