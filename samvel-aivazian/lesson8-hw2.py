from typing import List


class Item:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity

    def __str__(self) -> str:
        return f"Item: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Order:
    def __init__(self) -> None:
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)
        print(f"Added {item.quantity} x {item.name} to the order.")

    def calculate_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

    def finalize_purchase(self) -> None:
        total = self.calculate_total()
        print(f"Order finalized. Total: ${total:.2f}")

    def display_order(self) -> None:
        print("Current order:")
        for item in self.items:
            print(f"  {item}")
        print(f"Total: ${self.calculate_total():.2f}")


def main() -> None:
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
