class Ziemniak:
    def __init__(self, sort_name, dimension, price):
        self.sort_name = sort_name
        self.dimension = dimension
        self.price = price

    def calculate_order_value(self, amount):
        order_value = amount * self.price
        print(f"Całkowita wartość zamówienia na {amount} kg ziemniaków {self.sort_name} wynosi {order_value} zł.")

    def __repr__(self):
        return f"<class Ziemniak: sort_name={self.sort_name}, dimension={self.dimension}, price={self.price}>"


ziemniak_1 = Ziemniak(sort_name="Niwa", dimension=5, price=1.5)
ziemniak_2 = Ziemniak(sort_name="Luga", dimension=8, price=1.0)
ziemniak_3 = Ziemniak(sort_name="Luksusowy", dimension=15, price=2.4)

print(repr(ziemniak_1))
print(repr(ziemniak_2))
print(repr(ziemniak_3))

ziemniak_3.calculate_order_value(amount=3)
ziemniak_2.calculate_order_value(amount=10)
ziemniak_1.calculate_order_value(amount=25)
