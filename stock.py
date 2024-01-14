import csv
from decimal import Decimal


class Stock:
    types = [str, int, float]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, num_shares):
        self.shares = self.shares - num_shares

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    @staticmethod
    def read_portfolio(filename):
        portfolio = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                portfolio.append(Stock.from_row(row))
        return headers, portfolio

    @staticmethod
    def print_portfolio(portfolio):
        dashes = '-' * 10
        name = 'name'
        shares = 'shares'
        price = 'price'
        print(f'{name:>10} {shares:>10} {price:>10}')
        print(f'{dashes:>10} {dashes:>10} {dashes:>10}')
        for row in portfolio:
            print(f'{row.name:>10} {row.shares:>10} {row.price:>10}')

class DStock(Stock):
    types = (str, int, Decimal)


