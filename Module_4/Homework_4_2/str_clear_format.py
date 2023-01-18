def clear_your_name_format():
    name = input("Jakie jest Twoje imię?")
    last_name = input("A jak masz na nazwisko?")
    name = name.strip()
    last_name = last_name.strip()
    message = "Nazywasz się {} {}. Miło Cię poznać :)".format(name, last_name)
    print(message)

