import random


def generate_list():
    lista = []
    for _ in range(random.randint(1, 20)):
        lista.append(random.randint(1, 100))
    return lista
