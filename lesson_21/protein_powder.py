from food import Food
class ProteinPowder(Food):
    def __init__(self, name, price, protein):
        self.name = name
        self.price = price
        self.protein = protein
    def is_high_protein(self):
        return print(f"蛋白含量高嗎? answer: {self.protein > 20}")