from order import Order

class Coffee:
    _all = []

    def __init__(self, name):
        self.name = name
        Coffee._all.append(self)

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Coffee name must be a string")
        if len(value) < 3:
            raise Exception("Coffee name must be at least 3 characters long")
        
        self._name = value
        

    def orders(self):
        return[order for order in Order._all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})