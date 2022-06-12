from .product_characteristics import find_product_by_name, update_available_amount

order_list = []


def create_order_list(name, amount):
    product = find_product_by_name(name)
    order = {}
    if amount > product["available_amount"]:
        print(f"Niestety w sklepie dostępna jest tylko ilość {product['available_amount']} produktu {product['name']}. Zamówię tylko tę ilość.")
        amount = product["available_amount"]
    if product["name"] == name:
        order = {"order_name": name,
                 "order_amount": amount,
                 "order_cost": (product["price"] * amount)}
    order_list.append(order)
    update_available_amount(name, amount)
    return order_list
