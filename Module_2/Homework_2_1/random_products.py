import random
from Module_2.Homework_2_1.classess_objects import Produkt, Zamowienie
from Module_2.Homework_2_1.print_functions import print_zamowienie


def create_random_order():
    number_of_products = random.randint(1, 20)
    product_list = []
    print("-"*20)
    for product_number in range(number_of_products):
        product = Produkt(name=f"Produkt_{product_number}", category_name="random", price=random.randint(1, 100))
        product_list.append(product)

    order = Zamowienie(first_name="X", last_name="Y", product_list=product_list)
    return order


def run_order():
    order = create_random_order()
    print_zamowienie(order)


if __name__ == "__main__":
    run_order()

print(__name__)
