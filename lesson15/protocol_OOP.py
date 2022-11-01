from typing import List, Protocol


class Item(Protocol):
    quantity: int
    price: float


class Product:
    def __init__(self, product_name: str, quantity: int, price: float, currency: str):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.currency = currency



class Stock:
    def __init__(self, company_name: str, quantity: int, price: float, currency: str):
        self.company_name = company_name
        self.quantity = quantity
        self.price = price
        self.currency = currency

purchases = [
    Product('PC', 10, 350.0, 'USD'),
    Product('Laptop', 15, 550.0, 'USD'),
    Stock('AAPL', 100, 55.67, 'USD'),
    Stock('NYT', 53, 77.13, 'USD')
]

def calculate_total(items: List[Item]):
    return round(sum([item.quantity * item.price for item in items]), 2)

if __name__ == '__main__':
    total = calculate_total(purchases)
    print(total)
