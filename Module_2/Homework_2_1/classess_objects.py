class Produkt:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price


product_1 = Produkt(name="szczypior", category_name="zielenina", price=30)
product_2 = Produkt(name="malinowy", category_name="pomidory", price=22)


def order_value_calculation(product_list):
    order_value = 0
    for product in product_list:
        order_value += product.price
    return order_value


class Zamowienie:
    def __init__(self, first_name, last_name, product_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if product_list is None:
            product_list = []
        self.product_list = product_list
        self.order_value = order_value_calculation(product_list)


class Jablko:
    def __init__(self, sort_name, dimension, price):
        self.sort_name = sort_name
        self.dimension = dimension
        self.price = price


jablko_1 = Jablko(sort_name="Gala", dimension=7, price=10)
jablko_2 = Jablko(sort_name="Cortland", dimension=11, price=15)
jablko_3 = Jablko(sort_name="Fantazja", dimension=9, price=21)


class Ziemniak:
    def __init__(self, sort_name, dimension, price):
        self.sort_name = sort_name
        self.dimension = dimension
        self.price = price


ziemniak_1 = Ziemniak(sort_name="Niwa", dimension=5, price=1.5)
ziemniak_2 = Ziemniak(sort_name="Luga", dimension=8, price=1.0)
ziemniak_3 = Ziemniak(sort_name="Luksusowy", dimension=15, price=2.4)

order_1 = Zamowienie(first_name="Marian", last_name="Woźniak", product_list=[product_1, product_2])
order_2 = Zamowienie(first_name="Jola", last_name="Nowak", product_list=[jablko_3, product_2, ziemniak_3, ziemniak_1])


if __name__ == "__main__":
    print(type(jablko_1))
    print(type(ziemniak_3))



