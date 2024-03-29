from Module_3.Homework_3_1.shop.discount_policy import DiscountPolicy


class Order:
    MAX_ELEMENTS = 5

    def __init__(self, client_first_name, client_last_name, order_elements=None, discount_policy=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name

        if order_elements is None:
            order_elements = []
        self._order_elements = order_elements

        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy
        # self.total_price = self._calculate_total_price()

    @property
    def total_price(self):
        total_price_before_discount = 0
        for element in self._order_elements:
            total_price_before_discount += element.calculate_price()
        return self.discount_policy.apply_discount(total_price_before_discount)

    # @property
    # def calculate_total_price(self):
    #     return self.total_price()

    @property
    def order_elements(self):
        return self._order_elements

    # @property
    # def total_price(self):
    #     return self.total_price()

    @order_elements.setter
    def order_elements(self, value):
        if len(value) < Order.MAX_ELEMENTS:
            self._order_elements = value
        else:
            print("Osiągnięto limit pozycji w zamówieniu!")
            self._order_elements = value[:Order.MAX_ELEMENTS]
        # self.total_price = self._calculate_total_price()

    # def add_product_to_order(self, product, quantity):
    #     if len(self._order_elements) < Order.MAX_ELEMENTS:
    #         new_element = OrderElement(product, quantity)
    #         self._order_elements.append(new_element)
    #         self.total_price = self._calculate_total_price()
    #     else:
    #         print("Osiągnięto limit pozycji w zamówieniu")

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self) != len(other):
            return False

        if self.client_first_name != other.client_first_name or self.client_last_name != other.client_last_name:
            return False

        for order_element in self._order_elements:
            if order_element not in other.order_elements:
                return False
        return True

    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN po rabacie."
        product_details = "Zamówione produkty:\n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, value_details, product_details, mark_line])
        return result

    def __len__(self):
        return len(self._order_elements)
