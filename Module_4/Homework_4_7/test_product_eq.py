from .product import Product


def test_product_eq():
    parameters = [
        ("jogurt", "jogurt", "nabiał", "nabiał", 10, 10, True),
        ("jogurt", "jogurt", "nabiał", "nabiał", 10, 10, False),
        ("jogurt", "mleko", "nabiał", "nabiał", 10, 5, False),
        ("mleko", "mleko", "nabiał", "nabiał", 5, 5, True)
    ]
    for params in parameters:
        name, other_name, category_name, other_category_name, unit_price, other_unit_price, expected_result = params
        product = Product(name, category_name, unit_price, 1)
        other_product = Product(other_name, other_category_name, other_unit_price, 2)
        result = product == other_product

        if result == expected_result:
            print("OK")

        else:
            print("Błąd! Dla parametrów: ")
            print(f"{name, other_name, category_name, other_category_name, unit_price, other_unit_price}")
            print(f"wynik porównania produktów to {result}, a powinien być {expected_result}.")


def run_test():
    test_product_eq()
