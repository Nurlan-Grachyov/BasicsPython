class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


f = Fibonacci()
for i in range(100):
    print(next(f))
