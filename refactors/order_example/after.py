from enum import Enum, auto
from dataclasses import dataclass, field


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class Item:
    name: str
    quantity: int
    price: int

    @property
    def calcualted_price(self) -> int:
        return self.quantity * self.price


@dataclass
class Order:
    items: list[Item] = field(default_factory=list)
    status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    @property
    def total_price(self) -> int:
        return sum([item.calcualted_price for item in self.items])


def main() -> None:
    order = Order()
    order.add_item(Item(name="Keyboard", quantity=1, price=5000))
    order.add_item(Item(name="SSD", quantity=1, price=15000))
    order.add_item(Item(name="USB cable", quantity=2, price=500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
