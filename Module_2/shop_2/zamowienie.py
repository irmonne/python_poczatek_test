import random
from Module_2.shop_2.order_element import order_element_1, order_element_2, OrderElement
from Module_2.shop_2.produkt import Produkt


class Zamowienie:
    def __init__(self, first_name, last_name, order_element_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if order_element_list is None:
            order_element_list = []
        self.order_element_list = order_element_list
        self.order_value = self.order_value_calculation()

    def order_value_calculation(self):
        order_value = 0
        for order_element in self.order_element_list:
            order_value += order_element.calculate_value()
        return order_value

    def __str__(self):
        order_elements = ""
        for order_element in self.order_element_list:
            order_elements += "\n"
            order_elements += str(order_element)
        return f"Składający zamówienie: {self.first_name} {self.last_name}, zamawiane produkty: {order_elements}, \n Wartość zamówienia: {self.order_value} zł"

    def __len__(self):
        return len(self.order_element_list)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.first_name == other.first_name and self.last_name == other.last_name and len(self.order_element_list) == len(other.order_element_list):
            for order_element in self.order_element_list:
                if order_element not in other.order_element_list:
                    return False
            return True
        return False


order_1 = Zamowienie(first_name="Marian", last_name="Woźniak", order_element_list=[order_element_1, order_element_2])
order_2 = Zamowienie(first_name="Marian", last_name="Woźniak", order_element_list=[order_element_1, order_element_2, order_element_1])

print(len(order_1))

print("Czy order_1 jest takie samo jak order_2?")
print(order_1 == order_2)


def create_random_order():
    number_of_order_elements = random.randint(1, 20)
    order_element_list = []
    for product in range(number_of_order_elements):
        product_name = f"produkt_{product+1}"
        product_category_name = f"X_{product+1}"
        product_price = random.randint(50, 300)
        product = Produkt(name=product_name, category_name=product_category_name, price=product_price)
        order_element = OrderElement(product, amount=random.randint(1, 200))
        order_element_list.append(order_element)

    order = Zamowienie(first_name="X", last_name="Y", order_element_list=order_element_list)
    return order


def run_order():
    order = create_random_order()
    print(str(order))
