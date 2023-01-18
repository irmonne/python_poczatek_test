import random


# def generate_all_digits_set(number_set=None):
#     if number_set is None:
#         number_set = set()
#     all_digits_set = {_ for _ in range(0, 11)}
#     while not all_digits_set.issubset(number_set):
#         additional_number = random.randint(0, 10)
#         number_set.add(additional_number)
#         print(f"Uzyskany zbiór pośredni: {number_set}")
#         print(f"Do tej pory uzyskano następujące liczby od 0 do 10: {number_set.intersection(all_digits_set)}")
#     print(f"Kompletny zbiór końcowy: {number_set}")
#
#
# if __name__ == "__main__":
#     generate_all_digits_set({50, 40, 66})
#
#
# def generate_all_digits_frozenset(frozen_set):
#     all_digits_set = {_ for _ in range(0, 11)}
#     unfrozen_set = set(frozen_set)
#     while not all_digits_set.issubset(unfrozen_set):
#         additional_number = random.randint(0, 10)
#         unfrozen_set.add(additional_number)
#         print(f"Uzyskany zbiór pośredni: {unfrozen_set}")
#         print(f"Do tej pory uzyskano następujące liczby od 0 do 10: {unfrozen_set.intersection(all_digits_set)}")
#     print(f"Kompletny zbiór końcowy: {unfrozen_set}")
#
#
# if __name__ == "__main__":
#     generate_all_digits_frozenset(frozenset({50, 40, 66}))


def generate_all_digits_set(some_set=None):
    if some_set is None:
        some_set = set()
    all_digits_set = {_ for _ in range(0, 11)}
    unfrozen_united_set = set(some_set)
    while not all_digits_set.issubset(unfrozen_united_set):
        additional_number = random.randint(0, 10)
        unfrozen_united_set.add(additional_number)
        print(f"Uzyskany zbiór pośredni: {unfrozen_united_set}")
        print(f"Do tej pory uzyskano następujące liczby od 0 do 10: {unfrozen_united_set.intersection(all_digits_set)}")
    print(f"Kompletny zbiór końcowy: {unfrozen_united_set}")


if __name__ == "__main__":
    generate_all_digits_set(frozenset({14, 47, 90}))
