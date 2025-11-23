from order import Order

class Customer:
    _all = []


    def __init__(self, name):
        self.name = name
        Customer._all.append(self)


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise Exception("Customer name must be between 1 and 15 characters")
        self._name = value


    def orders(self):
        return [order for order in Order.all if order.customer ==self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    

    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    