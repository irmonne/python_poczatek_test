# def default_policy(total_price):
#     return total_price
#
#
# def loyal_customer_policy(total_price):
#     return 0.95 * total_price
#
#
# def christmas_policy(total_price):
#     if total_price > 100:
#         return total_price - 20
#     return total_price


class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price


class PercentageDiscount(DiscountPolicy):

    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_price):
        return total_price*(1-self.percentage/100)


class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, discount):
        self.discount = discount

    def apply_discount(self, total_price):
        if total_price - self.discount >= 0:
            return total_price - self.discount
        else:
            print(f"Wartość zamówienia nie może być mniejsza niż {self.discount} PLN!")
            return 0
