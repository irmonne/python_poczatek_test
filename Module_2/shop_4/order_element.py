from Module_2.shop_4.produkt import product_1, product_2


class OrderElement:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount

    def calculate_value(self):
        return self.amount * self.product.price

    def __str__(self):
        return f"W tej pozycji zamówienia jest {self.amount} szt. produktu {self.product.name}. Jej wartość wynosi {self.calculate_value()} zł."

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.amount == other.amount


order_element_1 = OrderElement(product_1, 10)
order_element_2 = OrderElement(product_2, 20)


def compare_order_elements():
    print("Czy order_element_1 jest taki sam jak order_element_2?")
    print(order_element_1 == order_element_2)
