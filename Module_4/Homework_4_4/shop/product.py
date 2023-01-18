class Product:

    def __init__(self, name, category_name, unit_price, identifier):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price
        self.identifier = identifier

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.category_name == other.category_name and
                self.unit_price == other.unit_price)

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price} PLN/szt"


class ProductWithExpiry(Product):

    def __init__(self, name, category_name, unit_price, production_year, years_to_expiry):
        super().__init__(name, category_name, unit_price)
        self.production_year = production_year
        self.years_to_expiry = years_to_expiry

    def does_expire(self, current_year):
        if current_year - self.production_year > self.years_to_expiry:
            print(f"Data ważności produktu {self.name} już minęła!")
        else:
            print(f"Produkt {self.name} jest jeszcze ważny!")
