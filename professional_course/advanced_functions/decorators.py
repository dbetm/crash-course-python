""" It's a special closure: A decorator is a function which receives a
function as parameter, add things to the function and return it.
"""
def decorator(funct):
    def wrapper():
        print('This is extra!')
        funct()

    return wrapper

# Rustic way
def greet():
    print('Hello world!')

greet = decorator(greet)
greet()

# Pythonic way
@decorator
def saludar():
    print('Hola mundo')
saludar()
