import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


def inventory_manager():
    inventory = {}

    @execution_time_decorator
    def manage(command, item, quantity):
        if command == "add":
            if item in inventory:
                inventory[item] += quantity
            else:
                inventory[item] = quantity
        elif command == "update":
            inventory[item] = quantity
        logging.info(f"Inventory after {command}: {inventory}")

    return manage


if __name__ == "__main__":
    manage_inventory = inventory_manager()
    manage_inventory("add", "sword", 1)
    manage_inventory("add", "shield", 1)
    manage_inventory("update", "sword", 2)
