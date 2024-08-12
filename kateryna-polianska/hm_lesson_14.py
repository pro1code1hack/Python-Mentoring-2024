"""
Task 1: Inventory Manager

Implement a function that handles adding and updating an inventory for a fantasy game character using higher-order functions.

"""

def inventory_manager():
    inventory = {}
    
    def manage(command, item, quantity):
        nonlocal inventory
        
        if command == "add":
            if item in inventory:
                inventory[item] += quantity
            else:
                inventory[item] = quantity
        elif command == "update":
            inventory[item] = quantity
        else:
            print("Invalid command")
        
        return inventory
    
    return manage

def main():
    # Create an inventory manager instance
    manage = inventory_manager()
    
    # Example interactions with the inventory manager
    print(manage("add", "sword", 1))       # Output: {'sword': 1}
    print(manage("add", "shield", 1))      # Output: {'sword': 1, 'shield': 1}
    print(manage("add", "sword", 2))       # Output: {'sword': 3, 'shield': 1}
    print(manage("update", "shield", 5))   # Output: {'sword': 3, 'shield': 5}
    print(manage("update", "potion", 3))   # Output: {'sword': 3, 'shield': 5, 'potion': 3}
    print(manage("invalid", "potion", 3))  # Output: Invalid command

if __name__ == "__main__":
    main()


"""
Task 3: Music Composer

Implement a system that lets users compose their own music by adding notes and applying effects using higher-order functions.

"""

def add_notes(*notes):
    """Creates a list of musical notes."""
    return list(notes)

def echo_effect(notes):
    """Creates an echo effect by repeating the sequence of notes."""
    return notes + notes

def speed_change(notes, factor):
    """Changes the speed of the notes by taking every nth note based on the factor."""
    return notes[::factor]

def compose_music(notes, *effects):
    """Applies a series of effects to the notes using function composition."""
    for effect in effects:
        notes = effect(notes)
    return notes

def main():
    # Create a new composition
    notes = add_notes("C", "D", "E", "F")
    print(f"Original Composition: {notes}")

    # Apply echo effect
    echoed = compose_music(notes, echo_effect)
    print(f"Echoed Composition: {echoed}")

    # Apply speed change
    faster = compose_music(echoed, lambda n: speed_change(n, 2))
    print(f"Faster Composition: {faster}")

if __name__ == "__main__":
    main()
