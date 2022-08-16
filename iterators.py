from time import sleep


class FiboIter():

    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0

        return self

    def __next__(self):

        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            if self.max == 0:
                raise StopIteration
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            if self.max:
                if self.max == 1:
                    raise StopIteration
                if self.aux > self.max:
                    raise StopIteration

            return self.aux


if __name__ == '__main__':
    fibo = FiboIter(10000000)
    for num in fibo:
        print(num)
        sleep(0.05)
