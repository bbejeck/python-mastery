import unittest
import pytest
from stock import Stock


class TestStock(unittest.TestCase):
    def test_create(self):
        """ Test creating a stock object """
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_keyword(self):
        s = Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = Stock('GOOG', 100, 490.1)
        s.sell(25)
        self.assertEqual(s.shares, 75)

    def test_from_row(self):
        s = Stock.from_row(['GOOG', '100', '490.1'])
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        a = Stock('GOOG', 100, 490.1)
        b = Stock('GOOG', 100, 490.1)
        self.assertTrue(a == b)

    # Tests for failure conditions
    def test_shares_badtype(self):
        s = Stock('GOOG', 100, 490.1)
        with pytest.raises(TypeError):
            s.shares = '50'

    def test_shares_badvalue(self):
        s = Stock('GOOG', 100, 490.1)
        with pytest.raises(ValueError):
            s.shares = -50

    def test_price_badtype(self):
        s = Stock('GOOG', 100, 490.1)
        with pytest.raises(TypeError):
            s.price = '45.23'

    def test_price_badvalue(self):
        s = Stock('GOOG', 100, 490.1)
        with pytest.raises(ValueError):
            s.price = -45.23

    def test_bad_attribute(self):
        s = Stock('GOOG', 100, 490.1)
        with pytest.raises(AttributeError):
            s.share = 100


if __name__ == "__main__":
    unittest.main()
