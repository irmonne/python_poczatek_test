def print_kwargs(**kwargs):
    print(f"Argumenty przyjmują następującą wartość:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")
