from Module_2.Homework_unpacking_operators.print_args import print_args
from Module_2.Homework_unpacking_operators.print_kwargs import print_kwargs
from Module_2.Homework_unpacking_operators.list_merge import generate_list
from Module_2.Homework_unpacking_operators.dict_merge import dict_2, dict_3, dict_1


def run_homework():
    final_res = print_args("a", "b", "c", 6, 8)
    print(final_res)
    print(50*"-")
    print_kwargs(imię="Mikołaj", wiek=55, zawód="nauczyciel")
    print(50 * "-")
    lista_1 = generate_list()
    lista_2 = generate_list()
    print(lista_1)
    print(lista_2)
    lista_3 = [*lista_1, *lista_2]
    print(lista_3)
    print(50 * "-")
    print(dict_1)
    print(dict_2)
    print(dict_3)
    print_kwargs(**dict_3)


if __name__ == "__main__":
    run_homework()