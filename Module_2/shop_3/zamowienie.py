import random
from Module_2.shop_3.order_element import order_element_1, order_element_2, OrderElement
from Module_2.shop_3.produkt import Produkt, product_2


class Zamowienie:

    MAX_ORDER_ELEMENT_NO = 5

    def __init__(self, first_name, last_name, order_element_list=None):
        self.first_name = first_name
        self.last_name = last_name
        if order_element_list is None:
            order_element_list = []
        if len(order_element_list) > Zamowienie.MAX_ORDER_ELEMENT_NO:
            order_element_list = order_element_list[:Zamowienie.MAX_ORDER_ELEMENT_NO]
        self._order_element_list = order_element_list
        self.order_value = self._order_value_calculation()

    def _order_value_calculation(self):
        order_value = 0
        for order_element in self._order_element_list:
            order_value += order_element.calculate_value()
        return order_value


    def __str__(self):
        order_elements = ""
        for order_element in self._order_element_list:
            order_elements += "\n"
            order_elements += str(order_element)
        return f"Składający zamówienie: {self.first_name} {self.last_name}, zamawiane produkty: {order_elements} \nWartość zamówienia: {self.order_value} zł"

    def __len__(self):
        return len(self._order_element_list)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.first_name == other.first_name and self.last_name == other.last_name and len(self._order_element_list) == len(other._order_element_list):
            for order_element in self._order_element_list:
                if order_element not in other._order_element_list:
                    return False
            return True
        return False

    @classmethod
    def create_random_order(cls):
        number_of_order_elements = random.randint(1, cls.MAX_ORDER_ELEMENT_NO)
        _order_element_list = []
        for product in range(number_of_order_elements):
            product_name = f"produkt_{product+1}"
            product_category_name = f"X_{product+1}"
            product_price = random.randint(50, 300)
            product = Produkt(name=product_name, category_name=product_category_name, price=product_price)
            order_element = OrderElement(product, amount=random.randint(1, 200))
            _order_element_list.append(order_element)

        order = Zamowienie(first_name="X", last_name="Y", order_element_list=_order_element_list)
        return order

    def add_order_element(self, product, amount):
        if len(self._order_element_list) < Zamowienie.MAX_ORDER_ELEMENT_NO:
            order_element = OrderElement(product=product, amount=amount)
            self._order_element_list.append(order_element)
            self.order_value = self._order_value_calculation()
            return self
        else:
            print("Zamówienie nie może już zostać powiększone.")


order_1 = Zamowienie(first_name="Marian", last_name="Woźniak", order_element_list=[order_element_1, order_element_2])
order_2 = Zamowienie(first_name="Marian", last_name="Woźniak", order_element_list=[order_element_1, order_element_2, order_element_1])


def run_order():
    print(len(order_1))
    print("Czy order_1 jest takie samo jak order_2?")
    print(order_1 == order_2)
    print("-"*50)
    order_x = Zamowienie.create_random_order()
    print(order_x)
    print(f"W zamówieniu może być maksymalnie {Zamowienie.MAX_ORDER_ELEMENT_NO} pozycji zamówienia.")
    print("-" * 50)
    order_y = order_x.add_order_element(product=product_2, amount=111)
    if len(order_x._order_element_list) < Zamowienie.MAX_ORDER_ELEMENT_NO:
        print(order_y)
    print(f"W zamówieniu może być maksymalnie {Zamowienie.MAX_ORDER_ELEMENT_NO} pozycji zamówienia.")
