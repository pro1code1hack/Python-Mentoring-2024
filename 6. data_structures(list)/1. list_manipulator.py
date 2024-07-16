# Create a program that allows the user to manipulate a list in various ways. 
# The user can choose to add, remove, or modify items in the list

# Example of how the program should work
# Menu:
# 1. Add an item
# 2. Remove an item
# 3. Modify an item

# User chooses option 1:
# Enter the item to add: Apple
# Output: List: ['Apple']

# # User chooses option 2:
# Enter the item to remove: Apple
# Output: List: []

# # User chooses option 3:
# Enter the item to modify: Apple
# Enter the new item: Banana
# Output: List: ['Banana']


output = []

while True:

    print("Menu:", "1. Add an item", "2. Remove an item", "3. Modify an item", "0. Exit", sep="\n", end="\n")
    print()
    option = int(input("Choose an option: 1, 2, 3, or 0: "))

    if option == 1:
        item_to_add = input("Enter the item to add: ")
        output.append(item_to_add)
        print("List: ", output)
      
    elif option == 2:
        if len(output) == 0:
            print("Nothing to revome yet", "____________", sep="\n")
            
        else:
            item_to_remove = input("Enter the item to remove: ")
            output.remove(item_to_remove)
            print("List: ", output)

    elif option == 3:
        if len(output) == 0:
            print("Nothing to modify yet", "____________", sep="\n")
           
        else:
            item_to_modify, new_item = input("Enter the item to modify and a new item (Banana Apple): ").split(" ")
            mod_index = output.index(item_to_modify)
            output.insert(mod_index, new_item)
            output.remove(item_to_modify)
            print("List: ", output)
        
    elif option == 0:
        print("Exit", "____________", sep="\n")
        break




