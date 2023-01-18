from Module_2.shop_3.produkt import product_1, product_2, product_3, product_4
from Module_2.shop_3.zamowienie import order_1, run_order
from Module_2.shop_3.taxcalculator import run_taxcalculator


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
