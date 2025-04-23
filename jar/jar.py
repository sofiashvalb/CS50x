def main():
    jar = Jar()
    print(str(jar.capacity))
    jar.deposit(2)
    jar.withdraw(1)
    print(str(jar))

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            #warning massege to the user for something being wrong:
            raise ValueError('Wrong capacity')
        #initialize the capacity of the jar for self and the size.
        self._capacity = capacity
        self._size = int(input("number of cookies: "))

    def __str__(self):
        #take the (size)number of cookies and multiplies by the emoji
        return self.size * '🍪'

    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError('Wrong capacity')
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            ValueError('Wrong capacity')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

main()
