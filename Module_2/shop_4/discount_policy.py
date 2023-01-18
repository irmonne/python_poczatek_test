class DiscountPolicy:

    @staticmethod
    def default_order_value_calculation(order_element_list):
        order_value = 0
        for order_element in order_element_list:
            order_value += order_element.calculate_value()
        return order_value

    @staticmethod
    def no_discount_policy(order_element_list):
        return DiscountPolicy.default_order_value_calculation(order_element_list)

    @staticmethod
    def regular_customer_discount_policy(order_element_list):
        return DiscountPolicy.default_order_value_calculation(order_element_list)*0.95

    @staticmethod
    def christmas_discount_policy(order_element_list):
        if DiscountPolicy.default_order_value_calculation(order_element_list) > 100:
            return DiscountPolicy.default_order_value_calculation(order_element_list)-20
        return DiscountPolicy.default_order_value_calculation(order_element_list)
