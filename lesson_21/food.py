
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def is_high_price(self):
        return self.price > 100