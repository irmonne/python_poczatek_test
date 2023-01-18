import random


def generate_identifier():
    raw_identifier = random.randint(1, 9999)
    print(raw_identifier)
    identifier = str(raw_identifier).zfill(5)
    print(identifier)
