def clear_your_name():
    name = input("Jakie jest Twoje imię?")
    last_name = input("A jak masz na nazwisko?")
    name = name.strip()
    last_name = last_name.strip()
    print(f"Nazywasz się {name} {last_name}. Miło Cię poznać :)")
