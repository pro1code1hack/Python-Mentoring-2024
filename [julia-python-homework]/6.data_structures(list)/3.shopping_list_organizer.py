"""Develop a program that helps users organize their shopping list
by adding, viewing, removing and sort items alphabetically.
Additionaly, we would want to check if we add strings to the list."""

output = []

while True:

    print(
        "Menu:",
        "1. Add item",
        "2. View list",
        "3. Remove item",
        "4. Exit",
        sep="\n",
        end="\n",
    )
    print()
    option = input("Choose an option: add, view, remove, exit: ")

    if option == "add":
        item_to_add = input("Enter an item to add: ")
        try:
            if int(item_to_add):
                print("Sorry, it is not a string..")
        except ValueError:
            if isinstance(item_to_add, str):
                output.append(item_to_add)
                print("Item added. Your current list is: ", output)

    elif option == "remove":
        if len(output) == 0:
            print(
                "Your shopping List is empty. Nothing to revome yet",
                "____________",
                sep="\n",
            )

        else:
            item_to_remove = input("Enter an item to remove: ")
            output.remove(item_to_remove)
            print("Item removed. Your current list is: ", output)

    elif option == "view":
        if len(output) == 0:
            print("Your shopping List is empty", "_____________", sep="\n")

        else:
            print("Your shopping List: ", output)

    elif option == "exit":
        print("Exiting the program", "_________", sep="\n")
        break
