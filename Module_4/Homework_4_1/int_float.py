import random
import math

float_1 = random.uniform(-20, 20)
float_2 = random.uniform(-20, 20)
float_3 = random.uniform(-20, 20)
float_4 = random.uniform(-20, 20)
float_5 = random.uniform(-20, 20)
float_6 = random.uniform(-20, 20)

int_1 = random.randint(1, 10)
int_2 = random.randint(1, 10)
int_3 = random.randint(1, 10)

print(float_1, float_2, float_3, float_4, float_5, float_6, int_1, int_2, int_3, sep=", ")

print(round(float_1, ndigits=2))
print(math.ceil(float_2))
print(math.floor(float_3))
print(math.pow(float_4, int_1))
print(float_5 ** int_2)
print(pow(float_6, int_3))
