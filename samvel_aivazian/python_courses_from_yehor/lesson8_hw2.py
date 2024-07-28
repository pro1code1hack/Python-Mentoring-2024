from typing import List


class Item:
    """
    A class to represent an item in an order.

    Attributes:
    name (str): The name of the item.
    price (float): The price of the item.
    quantity (int): The quantity of the item.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity

    def __str__(self) -> str:
        return f"Item: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Order:
    """
    A class to represent an order containing multiple items.

    Attributes:
    items (List[Item]): A list of items in the order.
    """

    def __init__(self) -> None:
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """
        Add an item to the order.

        Args:
        item (Item): The item to add.
        """
        self.items.append(item)
        print(f"Added {item.quantity} x {item.name} to the order.")

    def calculate_total(self) -> float:
        """
        Calculate the total cost of the order.

        Returns:
        float: The total cost of the order.
        """
        return sum(item.price * item.quantity for item in self.items)

    def finalize_purchase(self) -> None:
        """
        Finalize the purchase of the order.
        """
        total = self.calculate_total()
        print(f"Order finalized. Total: ${total:.2f}")

    def display_order(self) -> None:
        """
        Display the current order details.
        """
        print("Current order:")
        for item in self.items:
            print(f"  {item}")
        print(f"Total: ${self.calculate_total():.2f}")


def main() -> None:
    """
    Main function to create items, add them to an order, and display the order details.
    """
    item1 = Item(name="Laptop", price=999.99, quantity=1)
    item2 = Item(name="Mouse", price=49.99, quantity=2)

    print(item1)
    print(item2)

    order = Order()
    order.add_item(item1)
    order.add_item(item2)

    order.display_order()

    order.finalize_purchase()


if __name__ == "__main__":
    main()
