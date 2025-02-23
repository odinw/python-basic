
class food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def is_high_price(self):
        return self.price > 100
    
beef_noodle = food("牛肉麵", 160)
print(beef_noodle.is_high_price())