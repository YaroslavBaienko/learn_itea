class Accaunt:
    def __init__(self, bought=0.00, sold=0.00, buy_goods=list(), sell_goods=list(), amount=0.0, currency='UAH'):
        self.amount = amount
        self.currency = currency
        self.buy_goods = buy_goods
        self.sell_goods = sell_goods
        self.bought = bought
        self.sold = sold

    def buy(self, cost: float, good: str):
        self.amount = self.amount - cost
        self.buy_goods.append(good)
        self.bought = self.bought + cost

    def sell(self, cost: float, good: str):
        self.amount = self.amount + cost
        self.sell_goods.append(good)
        self.sold = self.sold + cost


my_account = Accaunt(amount=1000.00, currency='UAH')
her_account = Accaunt(amount=2000.00, currency='UAH')

while True:
    choise = input('Купить - b, Продать - s: ')
    if choise == 'b':
        purchase = input("Введите товар, который вы хотите купить: ")
        cost = float(input("Введите цену за товар: "))
        my_account.buy(cost=cost, good=purchase)
    elif choise == 's':
        purchase = input("Введите товар, который вы хотите продать: ")
        cost = float(input("Введите цену за товар: "))
        my_account.sell(cost=cost, good=purchase)
    else:
        print('Введи корректные данные')
    print(
        f'Продано: {my_account.sell_goods} на общую сумму: {my_account.sold} {my_account.currency}, куплено: {my_account.buy_goods} на общую сумму {my_account.bought} {my_account.currency}')
    print(f'Всего на Вашем счету: {my_account.amount} {my_account.currency}')
