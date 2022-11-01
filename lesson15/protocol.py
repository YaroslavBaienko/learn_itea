from typing import List, Protocol


class Item(Protocol):
    quantity: int
    price: float


class Product:
    def __init__(self, product_name: str, quantity: int, price: float):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


class Stock:
    def __init__(self, company_name: str, quantity: int, price: float):
        self.company_name = company_name
        self.quantity = quantity
        self.price = price


def calculate_total_sum(items: List[Item]):
    return round(sum([item.quantity * item.price for item in items]), 2)


purchases = [
    Product('PC', 10, 350.0),
    Product('Notebook', 15, 550.0),
    Stock('APL', 100, 55.67),
    Stock('NYT', 53, 77.13),
]

if __name__ == '__main__':
    total = calculate_total_sum(purchases)
    print(total)
