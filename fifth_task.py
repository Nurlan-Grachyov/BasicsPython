from dataclasses import dataclass


@dataclass
class PercentDiscount:
    """There is no need to describe anything here."""
    value: float


@dataclass
class FixDiscount:
    """There is no need to describe anything here."""
    value: float


@dataclass
class LoyaltyDiscount:
    """There is no need to describe anything here."""
    value: float


@dataclass
class Order:
    """There is no need to describe anything here."""
    # Объявил заказ, скидки для каждых категорий.
    order: dict[str, dict[str, float | str]]
    discount_for_categories = {(PercentDiscount, FixDiscount, LoyaltyDiscount): ["list of product categories"],
                               (PercentDiscount, FixDiscount): ["list of product categories"],
                               (FixDiscount, LoyaltyDiscount): ["list of product categories"],
                               (PercentDiscount, LoyaltyDiscount): ["list of product categories"],
                               (PercentDiscount,): ["list of product categories"],
                               (FixDiscount,): ["list of product categories"],
                               (LoyaltyDiscount,): ["list of product categories"]}
    PercentFixLoyalty = (PercentDiscount, FixDiscount, LoyaltyDiscount)
    PercentFix = (PercentDiscount, FixDiscount)
    FixLoyalty = (FixDiscount, LoyaltyDiscount)
    PercentLoyalty = (PercentDiscount, LoyaltyDiscount)
    Percen = (PercentDiscount,)
    Fix = (FixDiscount,)
    Loyalty = (LoyaltyDiscount,)
    product_prices = []

    def choose_discount(self):
        """
        Проходим по order, забираем оттуда категорию и сравниваю ее категориями, имеющиеся у discount_for_categories,
        находим нужный кортеж категорий и высчитываем итоговую сумму товара.
        """

        for key, value in self.order.items():
            category = value.get("category")
            for key_cat, category_cat in self.discount_for_categories.items():
                if category_cat == category:
                    if key_cat == self.PercentFixLoyalty:
                        # здесь высчитываем итоговую цену каждого товара со всеми возможными скидками для этой категории
                        pass
                    elif key_cat == self.PercentFix:
                        pass
                    # и так далее
                    self.product_prices.append(price)

    def price_order(self):
        price_order = sum(self.product_prices)
        return price_order
