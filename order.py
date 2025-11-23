from customer import Customer
from coffee import Coffee

class order:
    all = []

    def __init__(self, costomer, coffee, price):
        self.costomer = price
        self.coffee = coffee
        self.price = price
        order.all.append(self)

    @property
    def customer(self):
        return self._customer
    

    @customer.setter
    def customer(self, value):
        if not isinstance(value,  Customer):
            raise Exception("Order.customer must be a Customer instance")
        self._customer = value


    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value,Coffee):
            raise Exception("Order.coffee must be a coffee instance")
        self._coffee = value


    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, ( int, float)):
            raise Exception("Price must be a number")
        if not (1.0 <= float(value) <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0")
        self._price = float(value)