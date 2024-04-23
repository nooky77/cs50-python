class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Not a positive integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        emoji = "\U0001F36A"
        return self._size * emoji

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Jar overflow, too much cookies.")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    test = Jar(10)
    test.deposit(5)
    test.withdraw(3)
    print(test)


main()
