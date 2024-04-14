# Task 1: List Manipulator
def list_manipulator() -> None:
    items = []  # Initial empty list

    def print_menu() -> None:
        print("\nMenu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Modify an item")
        print("0. Exit")

    while True:
        print_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            # Add an item
            item_to_add = input("Enter the item to add: ")
            
            items.append(item_to_add)
            print(f"Output: list: {items}")
        
        elif choice == "2":
            # Remove an item
            item_to_remove = input("Enter the item to remove: ")
            
            if item_to_remove in items:
                items.remove(item_to_remove)
            else:
                print("Item not found in the list.")
            
            print(f"Output: list: {items}")
        
        elif choice == "3":
            # Modify an item
            item_to_modify = input("Enter the item to modify: ")

            if item_to_modify in items:
                new_item = input("Enter the new item: ")
                index_to_modify = items.index(item_to_modify)
                items[index_to_modify] = new_item
            else:
                print("Item not found in the list.")
            
            print(f"Output: list: {items}")
        
        elif choice == "0":
            # Exit the program
            print("Exiting the program.\n")
            break

        else:
            print("Invalid option. Please try again.")


# Task 2: List Slicer and Dicer
def list_slicer_and_dicer() -> None:
    # User inputs a list of numbers
    numbers_input = input("Enter a list of numbers (separated by space): ")
    numbers_list = [int(item) for item in numbers_input.split()]

    # User inputs the start and stop indices for slicing
    start_index = int(input("Enter start index for slicing: "))
    stop_index = int(input("Enter stop index for slicing: "))

    # Perform slicing and print the result
    sliced_list = numbers_list[start_index:stop_index]
    print(f"The sliced list is: {sliced_list}")


list_manipulator()
list_slicer_and_dicer()