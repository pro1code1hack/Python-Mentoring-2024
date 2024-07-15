def display_menu() -> None:
    """Displays the menu options."""
    print("\nMenu:")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")


def add_item(shopping_list: list) -> None:
    """Adds an item to the shopping list."""
    item = input("Enter an item to add: ")
    if isinstance(item, str):
        if item not in shopping_list:
            shopping_list.append(item)
            shopping_list.sort()
            print(f"Item added. Your current list is: {shopping_list}")
        else:
            print(f"Item '{item}' is already in the list.")
    else:
        print("Sorry, it is not a string")


def view_list(shopping_list: list) -> None:
    """Displays the current shopping list."""
    print(f"Shopping List: {shopping_list}")


def remove_item(shopping_list: list) -> None:
    """Removes an item from the shopping list."""
    item = input("Enter an item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item removed. Your current list is: {shopping_list}")
    else:
        print(f"Item '{item}' is not in the list.")


def handle_add_item(shopping_list: list) -> None:
    """Handler for adding an item."""
    add_item(shopping_list)


def handle_view_list(shopping_list: list) -> None:
    """Handler for viewing the list."""
    view_list(shopping_list)


def handle_remove_item(shopping_list: list) -> None:
    """Handler for removing an item."""
    remove_item(shopping_list)


def main() -> None:
    """Main function to run the shopping list organizer."""
    shopping_list = []

    handlers = {
        'add': handle_add_item,
        'view': handle_view_list,
        'remove': handle_remove_item,
        'exit': lambda x: print("Exiting the program.")  # Handler for exiting the program
    }

    while True:
        display_menu()
        action = input("Choose an action (add/view/remove/exit): ").strip().lower()

        if action in handlers:
            if action == 'exit':
                handlers[action](shopping_list)
                break
            else:
                handlers[action](shopping_list)
        else:
            print("Invalid action. Please choose again.")


if __name__ == "__main__":
    main()
