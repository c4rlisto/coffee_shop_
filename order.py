# order.py

from typing import List
from customer import Customer
from coffee import Coffee

class Order:
    _all_orders: List["Order"] = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        # validate types
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")

        # use property setters for price validation
        self._customer = customer
        self._coffee = coffee
        self.price = price

        Order._all_orders.append(self)

    def __repr__(self):
        return f"Order(customer={self.customer!r}, coffee={self.coffee!r}, price={self.price:.2f})"

    # class access to all orders
    @classmethod
    def all_orders(cls) -> List["Order"]:
        return list(cls._all_orders)

    # customer property (read only)
    @property
    def customer(self) -> Customer:
        return self._customer

    # coffee property (read only)
    @property
    def coffee(self) -> Coffee:
        return self._coffee

    # price property with validation: float between 1.0 and 10.0 inclusive
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value):
        try:
            val = float(value)
        except (TypeError, ValueError):
            raise TypeError("price must be a number (float).")
        if val < 1.0 or val > 10.0:
            raise ValueError("price must be between 1.0 and 10.0 inclusive.")
        self._price = val
