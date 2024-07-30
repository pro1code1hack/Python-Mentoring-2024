"""Develop a program that stores detailed information about a person using nested lists."""

# Input:
# Enter your name: Alice
# Enter your age: 30
# Enter your hobbies (separated by commas): reading, gardening, gaming
# Enter your favorite foods (separated by commas): pizza, salad, ice cream
# Output:
# Personal Information:
# Name: Alice
# Age: 30
# Hobbies: ['reading', 'gardening', 'gaming']
# Favorite Foods: ['pizza', 'salad', 'ice cream']
# # Later on, the program can provide options to view, update and remove these details.


name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobbies = input("Enter your hobbies (separated by commas): ").split(", ")
foods = input("Enter your favourite foods (separated by commas): ").split(", ")

while True:
    option = input("Choose an option: view, add, remove, or exit: ")

    if option == "view":
        print("Personal Information:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Hobbies: {hobbies}")
        print(f"Favourite food: {foods}")

    if option == "add":
        to_add = input("What do you want to add: hobbies or foods? ")

        if to_add == "foods":
            item_to_add = input(f"Enter an item to add to {to_add}: ")
            foods.append(item_to_add)
            print("Your new favourite foods are: ", foods)

        elif to_add == "hobbies":
            item_to_add = input(f"Enter an item to add to {to_add}: ")
            hobbies.append(item_to_add)
            print("Your new hobbies are: ", hobbies)

        else:
            print("It's a wrong option...")

    elif option == "remove":
        to_remove = input("What do you want to remove: hobbies or foods? ")

        if to_remove == "foods":
            item_to_remove = input(f"Enter an item to remove from {to_remove}: ")
            foods.remove(item_to_remove)
            print("Your new favourite foods are: ", foods)

        elif to_remove == "hobbies":
            item_to_remove = input(f"Enter an item to remove from {to_remove}: ")
            hobbies.remove(item_to_remove)
            print("Your new hobbies are: ", hobbies)

        else:
            print("It's a wrong option...")

    elif option == "change":
        to_change = input("What do you want to change: name or age? ")

        if to_change == "name":
            name = input("Enter your new name: ")
            print("Your new name is: ", name)

        elif to_change == "age":
            age = int(input("Enter your new age: "))
            print("Your new age is: ", age)

        else:
            print("It's a wrong option...")

    elif option == "exit":
        print("Exiting...")
        break
