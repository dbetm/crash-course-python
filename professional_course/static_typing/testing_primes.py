from math import sqrt

def is_prime(n:int) -> bool:
    """ Return True if the given number (n) is prime
    """
    ans = True

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            ans = False
            break

    return ans


def run():
    pass

if __name__ == '__main__':
    run()
