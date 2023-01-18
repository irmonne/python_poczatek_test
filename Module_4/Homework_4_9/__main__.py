from Module_4.Homework_4_9.data_generator import generate_order_elements
from Module_4.Homework_4_9.dataclass_order import Order


def run_homework():
    my_order_elements = generate_order_elements()
    my_order = Order("Monika", "Ka", my_order_elements)
    print(my_order)


if __name__ == "__main__":
    run_homework()
