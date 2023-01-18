from Module_2.shop.produkt import product_1, product_2


class OrderElement:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount

    def calculate_value(self):
        return self.amount * self.product.price

    def print_order_element(self):
        print(f"W tej pozycji zamówienia jest {self.amount} szt. produktu {self.product.name}.")
        print(f"Całkowita wartość tej pozycji zamówienia wynosi {self.calculate_value()} zł.")


order_element_1 = OrderElement(product_1, 10)
order_element_2 = OrderElement(product_2, 20)
