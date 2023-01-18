class Produkt:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

    def __str__(self):
        return f"Produkt: {self.name}, kategoria: {self.category_name}, cena: {self.price} zł"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.name == other.name and self.category_name == other.category_name and self.price == other.price


product_1 = Produkt(name="szczypior", category_name="fruit & vegetables", price=30)
product_2 = Produkt(name="malinowy", category_name="fruit & vegetables", price=22)
product_3 = Produkt(name="frytki", category_name="food", price=50)
product_4 = Produkt(name="czekolada", category_name="sweets", price=77)


def compare_products():
    print(f"Czy product_1 jest taki sam jak product_2?")
    print(product_1 == product_2)
