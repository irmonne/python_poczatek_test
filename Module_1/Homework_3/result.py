import Calculations.calculations


print("Obliczę wartość Twojej lokaty po określonym czasie :)")
start_value = int(input("Jaka jest początkowa wartość Twojej lokaty w złotych?\n"))
percentage = float(input("Jaka jest wartość oprocentowania w procentach?\n"))
time = int(input("Ile lat trzymasz pieniądze na lokacie?\n"))


end_value = Calculations.calculations.deposit_value(start_value, percentage, time)
print(f"Wartość końcowa Twojej lokaty po {time} latach wyniesie {end_value:.2f} złotych.")
