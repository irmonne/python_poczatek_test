from Module_3.Homework_3_1.shop.order import Order


class ExpressOrder(Order):

    EXPRESS_DELIVERY_PAYMENT = 10

    def __init__(self, delivery_deadline, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_deadline = delivery_deadline

    @property
    def total_price(self):
        return super().total_price + ExpressOrder.EXPRESS_DELIVERY_PAYMENT

    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Zamówienie ekspresowe złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN, w tym {self.EXPRESS_DELIVERY_PAYMENT} PLN opłaty za przesyłkę."
        delivery_deadline = f"Termin ekspresowej dostawy: {self.delivery_deadline}"
        product_details = "Zamówione produkty:\n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, value_details, delivery_deadline, product_details, mark_line])
        return result
