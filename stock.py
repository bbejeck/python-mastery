import csv


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, num_shares):
        self.shares = self.shares - num_shares

    @classmethod
    def read_portfolio(cls, filename):
        portfolio = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                portfolio.append(Stock(row[0], row[1], row[2]))
        return headers, portfolio

    @classmethod
    def print_portfolio(cls, headers, portfolio):
        dashes = '-' * 10
        print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10}')
        print(f'{dashes:>10} {dashes:>10} {dashes:>10}')
        for row in portfolio:
            print(f'{row.name:>10} {row.shares:>10} {row.price:>10}')

