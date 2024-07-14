def display_menu() -> None:
    print("\nMenu:")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")


def add_item(shopping_list: list) -> None:
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
    print(f"Shopping List: {shopping_list}")


def remove_item(shopping_list: list) -> None:
    item = input("Enter an item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item removed. Your current list is: {shopping_list}")
    else:
        print(f"Item '{item}' is not in the list.")


def main() -> None:
    shopping_list = []

    while True:
        display_menu()
        action = input("Choose an action (add/view/remove/exit): ").strip().lower()

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
            print("Invalid action. Please choose again.")


if __name__ == "__main__":
    main()
