import def_average_speed

mode = input("Podaj swój sposób poruszania się (bieg, jazda na rowerze, jazda samochodem):\n")
distance = float(input("Podaj przebytą odległość w km:\n"))
time = float(input("Podaj czas podróży w godz:\n"))
average_speed = def_average_speed.average_speed(distance, time)
print(f"W czasie podróży metodą {mode}, poruszałeś się ze średnią prędkością {average_speed:.2f} km/h.")
