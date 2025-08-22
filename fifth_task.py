from abc import ABC, abstractmethod


class Discount(ABC):
    """
    Абстрактный базовый класс для скидок.
    Требует реализовать метод apply для применения скидки к цене.
    """

    @abstractmethod
    def apply(self, price: float) -> float:
        """Применяет скидку к цене и возвращает новую цену."""
        pass


class PercentDiscount(Discount):
    """
    Скидка в процентах.
    """

    def __init__(self, value: float):
        self.value = value

    def apply(self, price: float) -> float:
        return price * (1 - self.value / 100)


class FixDiscount(Discount):
    """
    Фиксированная скидка в денежном выражении.
    """

    def __init__(self, value: float):
        self.value = value

    def apply(self, price: float) -> float:
        return max(0.0, price - self.value)


class LoyalDiscount(Discount):
    """
    Скидка для постоянных клиентов.
    """

    def __init__(self, value: float):
        self.value = value

    def apply(self, price: float) -> float:
        return max(0.0, price - self.value)


class Order:
    """
    Класс для обработки заказа с товарами и применяемыми скидками.
    """

    def __init__(self, items: list[dict]):
        """
        Список товаров, каждый в виде словаря с ключами 'category' и 'price'.
        """
        self.items = items
        # Скидки для каждой категории
        self.discounts = {
            "category": (
                LoyalDiscount(10.0),
                FixDiscount(150.0),
                PercentDiscount(5.0)
            )
        }

    def calculate_total(self) -> float:
        """
        Вычисляет итоговую сумму заказа с учетом скидок.
        """
        total = 0
        for product in self.items:
            category = product.get("category")
            price = product.get("price")
            # Применяем все скидки для категории
            for discount in self.discounts.get(category, []):
                price = discount.apply(price)
            total += price
        return total
