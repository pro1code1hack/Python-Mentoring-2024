"""
Task 2: Order System

Build an e-commerce order system where orders are composed of items,
but the lifecycle of items is independent of the order.

#### Requirements:
- Define an `Item` class with properties like `name`, `price`, and `quantity`.
- The `Order` class should be composed of `Item` objects and include methods to add items, calculate the total, and finalize the purchase.
- Items should be able to exist without being part of an order, indicating aggregation.
- Users should be able to create an order, add items, and see the order total.
- Users can also create standalone items that are not part of any order.

"""

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items)
        return total
    def finalize_purchase(self):
        total = self.calculate_total()
        self.items.clear()
        return total

if __name__ == "__main__":
    item1 = Item("Laptop", 1000, 1)
    item2 = Item("Mouse", 50, 2)
    order = Order()
    order.add_item(item1)
    order.add_item(item2)
    print("Order Total:", order.calculate_total())
    print("Finalizing Purchase. Total Amount:", order.finalize_purchase())









