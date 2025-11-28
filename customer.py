# customer.py

from typing import List, Optional
from order import Order
from coffee import Coffee

class Customer:
    _all_customers: List["Customer"] = []

    def __init__(self, name: str):
        self.name = name  # uses property setter validation
        Customer._all_customers.append(self)

    def __repr__(self):
        return f"Customer({self.name!r})"

    # name property with validation: string of length 1..15
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        value = value.strip()
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    # returns list of Order instances for this customer
    def orders(self) -> List[Order]:
        return [o for o in Order.all_orders() if o.customer is self]

    # returns unique list of Coffee instances this customer has ordered
    def coffees(self) -> List[Coffee]:
        coffees = []
        for o in self.orders():
            if o.coffee not in coffees:
                coffees.append(o.coffee)
        return coffees

    # create_order(coffee, price) -> new Order associated with this customer
    def create_order(self, coffee: Coffee, price: float) -> Order:
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        order = Order(self, coffee, price)
        return order

    # class method: returns Customer who spent the most on a particular coffee
    @classmethod
    def most_aficionado(cls, coffee: Coffee) -> Optional["Customer"]:
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        orders_for_coffee = [o for o in Order.all_orders() if o.coffee is coffee]
        if not orders_for_coffee:
            return None

        # sum spending per customer
        spending = {}
        for o in orders_for_coffee:
            c = o.customer
            spending[c] = spending.get(c, 0.0) + o.price

        # find customer with max spending (if tie, returns one of them)
        top_customer = max(spending.items(), key=lambda item: item[1])[0]
        return top_customer

    @classmethod
    def all_customers(cls) -> List["Customer"]:
        return list(cls._all_customers)
