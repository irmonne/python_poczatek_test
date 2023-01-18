list_a = [number for number in range(1, 31) if number % 3 == 0]
list_b = [number for number in range(1, 31) if number % 5 == 0]
print(list_a)
print(list_b)
list_a += list_b
print(list_a)
