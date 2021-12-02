import time

def fibo_gen(max=42):
    n1 = 0
    n2 = 1

    while True:
        yield n1

        n1, n2 = n2, n1 + n2

        if n1 > max:
            break


for x in fibo_gen():
    print(x)
    time.sleep(1)
