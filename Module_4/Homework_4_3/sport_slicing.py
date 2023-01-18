sports = str(input("Podaj listę swoich ulubionych sportów, rozdzielając je przecinkiem. "))
sports_list = sports.split(", ")
print(sports_list[1::2])
