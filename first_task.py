from dataclasses import dataclass


@dataclass
class Currency:
    name: str

    def __str__(self):
        return str(self.name)


@dataclass
class Money:
    value: float
    currency: str

    def __float__(self):
        return self.value


class Wallet:
    def __init__(self, currency):
        self.balance = {}
        self.currency = currency

    def __iadd__(self, other):
        if isinstance(other, Money):
            if other.currency != self.currency:
                raise ValueError("разные валюты")
            current_balance = self.balance.get(self.currency, 0)
            self.balance[self.currency] = current_balance + other.value
        elif isinstance(other, (int, float)):
            current_balance = self.balance.get(self.currency, 0)
            self.balance[self.currency] = current_balance + other.value
        return self

    def __isub__(self, other):
        if self.balance.get(self.currency, 0) < other.value:
            raise ValueError(f"в {self.currency} у тебя нет денег")
        if isinstance(other, Money):
            if other.currency != self.currency:
                raise ValueError("разные валюты")
            current_balance = self.balance.get(self.currency, 0)
            self.balance[self.currency] = current_balance - other.value
        elif isinstance(other, (int, float)):
            current_balance = self.balance.get(self.currency, 0)
            self.balance[self.currency] = current_balance - other.value
        return self

    def __getitem__(self, item):
        if item == 'balance':
            return f"{self.balance.get(self.currency)} {self.currency}"
        raise KeyError(f"Unknown key: {item}")


currency_ruble = str(Currency("rubles"))

money = Money(5000, currency_ruble)
money1 = Money(3000, currency_ruble)

operation_rubles = Wallet(currency_ruble)
try:
    operation_rubles += money
    print(operation_rubles['balance'])

    operation_rubles -= money1
    print(operation_rubles['balance'])
except ValueError as e:
    print(e)

currency_usd = str(Currency("usd"))

money_usd = Money(5000, currency_usd)
money_usd1 = Money(3000, currency_usd)
operation_rubles = Wallet(currency_usd)
try:
    operation_rubles += money_usd
    print(operation_rubles['balance'])

    operation_rubles -= money_usd1
    print(operation_rubles['balance'])
except ValueError as e:
    print(e)
