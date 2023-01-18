from Module_2.shop_4.produkt import product_1, product_2, product_3, product_4
from Module_2.shop_4.zamowienie import Zamowienie, order_1, run_order
from Module_2.shop_4.taxcalculator import run_taxcalculator


def add_new_order_element(order, product, amount):
    order.add_order_element(product, amount)
    print(order)


print("-"*50)

if __name__ == "__main__":
    print(product_1)
    print(product_2)

print("-"*50)

if __name__ == "__main__":
    print(order_1)

print("-"*50)

if __name__ == "__main__":
    run_order()

print("-"*50)

if __name__ == "__main__":
    run_taxcalculator(product_3, 100)
    run_taxcalculator(product_4, 200)

print("-"*50)

print(__name__)

print("-"*50)


def order_element_no_check(zamowienie):
    return len(zamowienie._order_element_list)


def generate_orders_sort_by_value():
    orders_list = []
    for _ in range(5):
        orders_list.append(Zamowienie.create_random_order())

    orders_list.sort(key=lambda zamowienie: zamowienie.order_value)
    for order in orders_list:
        print(order)
        print(sep="/n")


if __name__ == "__main__":
    generate_orders_sort_by_value()


print("-"*50)


def generate_orders_sort_by_or_el_no():
    orders_list = []
    for _ in range(5):
        orders_list.append(Zamowienie.create_random_order())

    orders_list.sort(key=order_element_no_check)
    for order in orders_list:
        print(order)
        print(sep="/n")


if __name__ == "__main__":
    generate_orders_sort_by_or_el_no()
