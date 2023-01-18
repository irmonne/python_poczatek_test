def print_args(*args):
    result = ""
    for arg in args:
        result += str(arg)
        result += " - "
    return result[:-3]

