# the variable 'a' is referenced by the nested function, even when the
# outer function is deleted.
def main():
    a = 42
    def nested():
        print(a)

    return nested

my_func = main()
print(my_func()) # 42

del(main)

print(my_func()) # 42

# ----------------------------------
def make_multiplier(x):
    def multiplier(n):
        return n * x

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # 30
print(times4(5)) # 20
print(times10(times4(2))) # 80


# Where to use closures?
"""
1. When we have a short/small class (one method).
2. When we have a decorator.
"""
