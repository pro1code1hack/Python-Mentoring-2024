"""
Task 1: Inventory Manager

Implement a function that handles adding and updating an inventory for a fantasy game character using higher-order functions.

**Requirements**:
- Write a `manage_inventory()` function that can take commands such as "add" or "update" along with item details and modifies the inventory accordingly.
- Use closures to encapsulate the inventory state within the manager.

"""

def inventory_manager():
    inventory = {}
    def manage(command, item, quantity):
        if command == "add":
            if item in inventory:
                inventory[item] += quantity
            else:
                inventory[item] = quantity
        elif command == "update":
            if item in inventory:
                inventory[item] = quantity
            else:
                print(f"Item '{item}' not found in inventory.")
        return inventory
    return manage









