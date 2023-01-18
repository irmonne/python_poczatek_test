class Jablko:
    def __init__(self, sort_name, dimension, price):
        self.sort_name = sort_name
        self.dimension = dimension
        self.price = price

    def calculate_order_value(self, amount):
        order_value = amount * self.price
        print(f"Całkowita wartość zamówienia na {amount} kg jabłek {self.sort_name} wynosi {order_value} zł.")


jablko_1 = Jablko(sort_name="Gala", dimension=7, price=10)
jablko_2 = Jablko(sort_name="Cortland", dimension=11, price=15)
jablko_3 = Jablko(sort_name="Fantazja", dimension=9, price=21)

jablko_3.calculate_order_value(amount=10)
jablko_2.calculate_order_value(amount=20)
jablko_1.calculate_order_value(amount=3)
