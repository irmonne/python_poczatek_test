def print_produkt(produkt):
    print(f"Produkt: {produkt.name}, kategoria: {produkt.category_name}, cena: {produkt.price} zł")


def print_zamowienie(zamowienie):
    print(f"Składający zamówienie: {zamowienie.first_name} {zamowienie.last_name}, zamawiane produkty:")
    for product in zamowienie.product_list:
        print_produkt(product)
    print(f"Wartość zamówienia: {zamowienie.order_value}")

