from collections import namedtuple

Apple = namedtuple("Apple", ["species_name", "size", "price"])

apple = Apple(species_name="Cortland", size=10, price=50)
print(apple.species_name, apple.size, apple.price, sep="\n")
print("-"*50)
print(apple[0], apple[1], apple[2], sep="; ")
print("-"*50)

for parameter in apple:
    print(parameter)

