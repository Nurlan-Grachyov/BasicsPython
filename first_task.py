class Money:
    def __init__(self, currency):
        self.balance = 0
        self.currency = currency

    def __add__(self, other):
        self.balance += other
        return f"{self.balance} {self.currency}"

    def __sub__(self, other):
        if self.balance < other:
            raise ValueError("Balance is less than withdrawal")
        self.balance -= other
        return f"{self.balance} {self.currency}"

    def __getitem__(self, item):
        return f"{self.__dict__.get(item)} {self.currency}"


operation_rubles = Money("Rubles")
print(operation_rubles.__getitem__("balance"))
print(operation_rubles.__add__(5000))
print(operation_rubles.__sub__(5000))

operation_usd = Money("USD")
print(operation_rubles.__getitem__("balance"))
print(operation_rubles.__add__(5000))
print(operation_rubles.__sub__(5000))
