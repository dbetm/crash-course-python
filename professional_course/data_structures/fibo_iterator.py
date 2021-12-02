import time


class FiboIter():

    def __init__(self, max=42):
        self.max = max

    def __iter__(self):
        self.n1, self.n2 = None, None
        return self

    def __next__(self):
        if self.n1 == None:
            self.n1 = 0
            ans = self.n1
        elif not self.n2:
            self.n2 = 1
            ans = self.n2
        else:
            ans = self.n1 + self.n2
            self.n1, self.n2 = self.n2, ans

        if ans > self.max:
            raise StopIteration

        return ans


if __name__ == '__main__':
    for x in FiboIter(100):
        print(x)
        time.sleep(1)
