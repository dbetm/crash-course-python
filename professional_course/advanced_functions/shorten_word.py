def shorten(funct):
    def wrapper(*args, **kwargs):
        processed_args = []
        for arg in args:
            if type(arg).__name__ == 'str' and len(arg) > 12:
                arg = arg[:2] + str(len(arg) - 4) + arg[-2:]
            processed_args.append(arg)
        funct(*processed_args)

    return wrapper


@shorten
def display_word(string: str):
    print(string)

display_word('gatito')
display_word('electrodinámica')
