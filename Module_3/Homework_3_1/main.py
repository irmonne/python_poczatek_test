
# Dodaj do programu obsługę polityki rabatowej.
# Zaimplementuj funkcje reprezentujące politykę podatkową i przekaż je do konstruktora zamówienia.
# Jeżeli polityka została przekazana to podczas liczenia łącznej kwoty zamówienia należy naliczyć rabat.
# Jeżeli nie - obliczamy łączną kwotę jak dotychczas.
# Zaimplementuj dwie polityki rabatowe:
# Dla stałych klientów: 5% rabatu na każdą pozycję
# Rabat świąteczny: rabat 20 PLN dla zamówień o łącznej kwocie powyżej 100 PLN

from shop.data_generator import generate_order_elements
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount, DiscountPolicy
from shop.order import Order
# from shop_1.product import ProductWithExpiry
from shop.express_order import ExpressOrder


# def run_homework():
#     first_name = "Mikołaj"
#     last_name = "Lewandowski"
#     order_elements = generate_order_elements()
#     normal_order = Order(first_name, last_name, order_elements)
#     loyal_customer_order = Order(first_name, last_name, order_elements, discount_policy=loyal_customer_policy)
#     christmas_order = Order(first_name, last_name, order_elements, discount_policy=christmas_policy)
#
#     print(normal_order)
#     print(loyal_customer_order)
#     print(christmas_order)
#
#
# if __name__ == '__main__':
#     run_homework()
#
#
# def run_getter_homework():
#     first_name = "Monika"
#     last_name = "Tufika"
#     order_elements = generate_order_elements()
#     order_with_getter = Order(first_name, last_name, order_elements)
#     print(order_with_getter)
#
#
# if __name__ == "__main__":
#     run_getter_homework()
#
#
# def run_setter_homework():
#     order_elements = generate_order_elements(7)
#     order = Order(client_first_name="Monika", client_last_name="Niefika", order_elements=order_elements)
#     print(order)
#
#
# if __name__ == "__main__":
#     run_setter_homework()
#
#
# def run_product_expiry_homework():
#     product_with_expiry = ProductWithExpiry("jogurt", "food", 3, 2020, 2)
#     product_with_expiry.does_expire(2023)
#
#
# if __name__ == "__main__":
#     run_product_expiry_homework()
#
#
# def run_express_delivery_homework():
#     order_elements = generate_order_elements()
#     express_order = ExpressOrder(
#         client_last_name="Gucio",
#         client_first_name="Miodek",
#         order_elements=order_elements,
#         delivery_deadline="29.09.2023"
#     )
#     print(express_order)
#
#
# if __name__ == "__main__":
#     run_express_delivery_homework()
#
#
# def run_discount_policy_homework():
#     percentage_discount = PercentageDiscount(percentage=10)
#     absolute_discount = AbsoluteDiscount(discount=20)
#
#     order_elements = generate_order_elements()
#
#     order_default = Order("Radek",
#                           "Nieporadek",
#                           order_elements)
#     print(order_default)
#     print("-"*50)
#
#     order_percentage = Order("Radek",
#                              "Nieporadek",
#                              order_elements,
#                              percentage_discount)
#
#     print(order_percentage)
#     print("-" * 50)
#
#     order_absolute = Order("Radek",
#                            "Nieporadek",
#                            order_elements,
#                            absolute_discount
#                            )
#     print(order_absolute)
#     print("-" * 50)
#
#
# if __name__ == "__main__":
#     run_discount_policy_homework()


