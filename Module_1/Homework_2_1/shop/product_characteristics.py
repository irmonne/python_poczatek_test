products = [
    {"name": "jabłka",
     "price": 3,
     "available_amount": 100},
    {"name": "chleb",
     "price": 2,
     "available_amount": 10},
    {"name": "czekolada",
     "price": 10,
     "available_amount": 20}
]


def find_product_by_name(name):
    for product in products:
        if product["name"] == name:
            return product


def is_product_in_shop(name):
    if not find_product_by_name(name):
        return False
    return True


def update_available_amount(name, ordered_amount):
    for product in products:
        if product["name"] == name:
            product["available_amount"] -= ordered_amount
