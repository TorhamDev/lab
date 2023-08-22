from enum import Enum, auto
from dataclasses import dataclass, field


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class Item:
    name: str
    price: str
    quantity: int

    @property
    def calcualted_price(self):
        return self.quantity * self.price


@dataclass
class Order:
    items: list[Item] = field(default_factory=list)
    status: str = PaymentStatus.OPEN

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(Item(name=name, quantity=quantity, price=price))

    @property
    def total_price(self) -> int:
        total = 0
        for item in self.items:
            total += item.calcualted_price

        return total


def main() -> None:
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
