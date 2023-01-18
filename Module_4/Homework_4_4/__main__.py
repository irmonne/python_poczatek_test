from shop import data_generator


def run_dict_compr_homework():
    order_elements = data_generator.generate_order_elements()
    print(order_elements)
    order_elements_dict = {order_element.product.identifier: order_element.product for order_element in order_elements}
    print(order_elements_dict)
    order_elements_dict_plus = {identifier + 1: product
                                for identifier, product in order_elements_dict.items()
                                }

    print(order_elements_dict_plus)

    order_elements_dict.update(order_elements_dict_plus)
    print(order_elements_dict)


if __name__ == "__main__":
    run_dict_compr_homework()
