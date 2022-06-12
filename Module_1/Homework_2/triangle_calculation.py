import math


print("Policzę długość przeciwprostokątnej trójkąta prostokątnego na podstawie długości przyprostokątnych.")
a = float(input("Podaj długość pierwszej przyprostokątnej trójkąta w cm.\n"))
b = float(input("Podaj długość pierwszej przyprostokątnej trójkąta w cm.\n"))


def triangle_calculation(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))


print(f"Długość przeciwprostokątnej trójkąta o przyprostokątnych długości {a} i {b} cm wynosi {triangle_calculation(a, b):.2f} cm.")
