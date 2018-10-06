from moneylib.converter import CurrencyConverter
from moneylib.money import Money
import unittest
from unittest.mock import MagicMock


class TestMoney(unittest.TestCase):

    def test_valid_transform(self):
        CurrencyConverter.convert = MagicMock(return_value=1)
        byr = Money(10)
        usd = Money(11, "USD")
        eur = Money(12.34, "EUR")
        self.assertEqual((byr + (usd * 3.11) + (eur * 0.8)).amount, 12)

    def test_substract(self):
        self.assertEqual((Money(10) - Money(11)).amount, -1)
        self.assertEqual((Money(10) - 3).amount, 7)
        self.assertEqual(
            float((Money(10.55, "USD") - Money(2, "USD")).amount), 8.55
        )

    def test_sum(self):
        self.assertEqual((Money(10) + Money(11)).amount, 21)
        self.assertEqual((Money(10) + 3).amount, 13)
        self.assertEqual(
            float((Money(10.55, "USD") + Money(2, "USD")).amount), 12.55
        )

    def test_multiply(self):
        self.assertEqual((Money(10) * Money(11)).amount, 110)
        self.assertEqual((Money(10) * 3).amount, 30)
        self.assertEqual(
            float((Money(10.55, "USD") * Money(2, "USD")).amount), 21.1
        )

    def test_divide(self):
        self.assertEqual(float((Money(10) / Money(5)).amount), 2)
        self.assertEqual((Money(10) / 4).amount, 2.5)
        self.assertEqual(
            float((Money(10.55, "USD") / Money(2, "USD")).amount), 5.275
        )


if __name__ == '__main__':
    # unittest.main()

    x = Money(10, "BYR")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(z + x * 3.11 + y * 0.8)  # result in “EUR”
