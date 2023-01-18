
# Zmodyfikuj rozwiązanie poprzedniego zadania. Skorzystaj z dict comprehensions
# aby na podstawie słownika z produktami stworzyć nowy, w którym każdy produkt będzie pod kluczem o 1 większym.
# I tak produkt, który znajdował się w oryginalnym słowniku pod kluczem 15 trafi w nowym pod klucz 16, itd.
# Następnie skorzystaj z metody update aby “połączyć” oba słowniki.
from Module_4.Homework_4_5.shop.data_generator import products_delivery

# def run_homework():
#     order_elements = data_generator.generate_order_elements()
#     identifier_to_product = {
#         order_element.product.identifier: order_element.product
#         for order_element in order_elements
#     }
#     moved_ids_to_product = {
#         identifier + 1: product
#         for identifier, product in identifier_to_product.items()
#     }
#
#     print(identifier_to_product)
#     print(moved_ids_to_product)
#
#     identifier_to_product.update(moved_ids_to_product)
#     print(identifier_to_product)
#
#
# if __name__ == '__main__':
#     run_homework()


def deliver_all_products():

    all_products = set(f"Product-{number}" for number in range(1, 10))
    delivered_products = products_delivery()
    print(f"Dowiezione produkty: {delivered_products}")
    delivered_products_set = set(delivered_products)

    while not all_products.issubset(delivered_products_set):
        print(f"Jeszcze potrzebne rodzaje produktów: {all_products.difference(delivered_products_set)}")
        next_delivered_products = products_delivery()
        print(f"Kolejne dowiezione produkty: {next_delivered_products}")
        next_delivered_products_set = set(next_delivered_products)
        delivered_products_set.update(next_delivered_products_set)
        print(f"Wszystkie dotychczas dowiezione rodzaje produktów: {delivered_products_set}")

    print("Wszystkie rodzaje produktów zostały już dostarczone.")


if __name__ == "__main__":
    deliver_all_products()
