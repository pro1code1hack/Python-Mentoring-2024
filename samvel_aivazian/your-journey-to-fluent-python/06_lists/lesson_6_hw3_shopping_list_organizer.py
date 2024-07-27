import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class ShoppingListOrganizer:
    def __init__(self):
        self.shopping_list = []

    def add_item(self, item):
        if isinstance(item, str):
            self.shopping_list.append(item)
            self.shopping_list.sort()
            logging.info(f"Item added. Your current list is: {self.shopping_list}")
        else:
            logging.info("Sorry, it is not a string.")

    def view_list(self):
        logging.info(f"Shopping List: {self.shopping_list}")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            logging.info(f"Item removed. Your current list is: {self.shopping_list}")
        else:
            logging.info("Item not found in the list.")


def main():
    organizer = ShoppingListOrganizer()

    while True:
        logging.info("Menu:")
        logging.info("1. Add item")
        logging.info("2. View list")
        logging.info("3. Remove item")
        logging.info("4. Exit")

        logging.info("Choose an action (add/view/remove/exit): ")
        choice = input().strip().lower()

        if choice == 'add':
            logging.info("Enter an item to add: ")
            item = input().strip()
            organizer.add_item(item)
        elif choice == 'view':
            organizer.view_list()
        elif choice == 'remove':
            logging.info("Enter an item to remove: ")
            item = input().strip()
            organizer.remove_item(item)
        elif choice == 'exit':
            logging.info("Exiting the program.")
            break
        else:
            logging.info("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
