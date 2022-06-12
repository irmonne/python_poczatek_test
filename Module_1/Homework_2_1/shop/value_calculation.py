from .product_characteristics import is_product_in_shop
from .order_creation import create_order_list


def calculate_order_value():

    final_order_list = []

    while True:
        order_name = input("Podaj nazwę zamawianego towaru albo zakończ wpisując 'X':\n")
        if order_name == "X":
            break
        if not is_product_in_shop(order_name):
            print(f"Niestety produktu {order_name} nie ma w sklepie...")
        else:
            order_amount = int(input(f"Podaj ilość zamawianego towaru w kategorii {order_name}:\n"))
            final_order_list = create_order_list(order_name, order_amount)

    order_value = 0
    for order in final_order_list:
        order_value += order["order_cost"]

    print(f"Całkowity koszt Twoich zakupów to {order_value} zł.")
