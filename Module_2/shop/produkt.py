class Produkt:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

    def print_produkt(self):
        print(f"Produkt: {self.name}, kategoria: {self.category_name}, cena: {self.price} zł")


product_1 = Produkt(name="szczypior", category_name="zielenina", price=30)
product_2 = Produkt(name="malinowy", category_name="pomidory", price=22)
