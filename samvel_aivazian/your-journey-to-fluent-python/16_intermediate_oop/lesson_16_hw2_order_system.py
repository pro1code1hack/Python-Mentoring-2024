import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price} x {self.quantity}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        logging.info(f"Added {item} to the order.")

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items)
        logging.info(f"Order total: ${total:.2f}")
        return total

    def finalize_purchase(self):
        total = self.calculate_total()
        logging.info(f"Purchase finalized. Total amount due: ${total:.2f}")


if __name__ == "__main__":
    item1 = Item("Laptop", 1000, 1)
    item2 = Item("Mouse", 50, 2)

    order = Order()
    order.add_item(item1)
    order.add_item(item2)

    order.calculate_total()
    order.finalize_purchase()
