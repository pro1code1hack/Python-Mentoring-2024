import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class ListManipulator:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        logging.info(f"List: {self.items}")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            logging.info(f"List: {self.items}")
        else:
            logging.info("Item not found in the list.")

    def modify_item(self, old_item, new_item):
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items[index] = new_item
            logging.info(f"List: {self.items}")
        else:
            logging.info("Item not found in the list.")


def main():
    manipulator = ListManipulator()

    while True:
        logging.info("Menu:")
        logging.info("1. Add an item")
        logging.info("2. Remove an item")
        logging.info("3. Modify an item")
        logging.info("4. Exit")

        logging.info("Choose an option: ")
        choice = input().strip()

        if choice == '1':
            logging.info("Enter the item to add: ")
            item = input().strip()
            manipulator.add_item(item)
        elif choice == '2':
            logging.info("Enter the item to remove: ")
            item = input().strip()
            manipulator.remove_item(item)
        elif choice == '3':
            logging.info("Enter the item to modify: ")
            old_item = input().strip()
            logging.info("Enter the new item: ")
            new_item = input().strip()
            manipulator.modify_item(old_item, new_item)
        elif choice == '4':
            break
        else:
            logging.info("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
