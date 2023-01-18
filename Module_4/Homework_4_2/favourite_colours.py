def is_blue_favourite():
    favourite_colours = input("Jakie są Twoje ulubione kolory?")
    if favourite_colours.lower().find("niebieski") == -1:
        print("Nie lubisz koloru niebieskiego :(")
    else:
        print("Wśród Twoich ulubionych kolorów jest niebieski :)")
