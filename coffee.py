# coffee.py

from typing import List
from order import Order
from customer import Customer

class Coffee:
    _all_coffees: List["Coffee"] = []

    def __init__(self, name: str):
        self.name = name  # uses property setter validation
        Coffee._all_coffees.append(self)

    def __repr__(self):
        return f"Coffee({self.name!r})"

    # name property validation: string at least 3 characters
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    # orders() -> list of Order instances for this coffee
    def orders(self) -> List[Order]:
        return [o for o in Order.all_orders() if o.coffee is self]

    # customers() -> unique list of Customer instances who ordered this coffee
    def customers(self) -> List[Customer]:
        customers = []
        for o in self.orders():
            if o.customer not in customers:
                customers.append(o.customer)
        return customers

    # num_orders() -> total number of times coffee has been ordered
    def num_orders(self) -> int:
        return len(self.orders())

    # average_price() -> average price across all orders for this coffee
    def average_price(self) -> float:
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(o.price for o in orders)
        return total / len(orders)

    @classmethod
    def all_coffees(cls) -> List["Coffee"]:
        return list(cls._all_coffees)
