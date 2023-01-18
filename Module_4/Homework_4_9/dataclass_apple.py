from dataclasses import dataclass


@dataclass
class Apple:
    species_name: str
    size: int
    price: float

    def calculate_price(self, quantity):
        return quantity * self.price
