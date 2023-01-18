import random

from Module_4.Homework_4_10.order import Order
from Module_4.Homework_4_10.order_element import OrderElement
from Module_4.Homework_4_10.product import Product
from Module_4.Homework_4_10.Enum_product_cat import ProductCategory

MIN_QUANTITY = 1
MAX_QUANTITY = 10

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 100


def generate_order_elements(products_to_generate=None) -> object:
    if products_to_generate is None:
        products_to_generate = random.randint(1, Order.MAX_ELEMENTS)

    order_elements = []
    for product_number in range(products_to_generate):
        product_name = f"Produkt-{product_number}"
        category_name = ProductCategory.OTHERS
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        identifier = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)
        product = Product(product_name, category_name, unit_price, identifier)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))

    return order_elements


def products_delivery():
    delivered_products = [f"Product-{random.randint(1, 10)}" for _ in range(5)]
    return delivered_products
