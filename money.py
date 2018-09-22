from currency import CURRENCIES_CODES
from decimal import Decimal
import requests


class CurrencyConverter(object):
    # better to have it in settings
    API_CLIENT_KEY = "<Some_API_key>"
    CONVERTER_ENDPOINT = "http://apilayer.net/api/convert?" \
                         "access_key={}&from={}&to={}&amount={}"
    UNSUPPORTED_OPERATION = "Unsupported operand type for {}: '{}' and '{}'"

    @classmethod
    def convert(cls, amount, from_currency, to_currency):
        try:
            response = requests.get(
                cls.CONVERTER_ENDPOINT.format(
                    cls.API_CLIENT_KEY,
                    from_currency,
                    to_currency,
                    amount
                )
            )
        except Exception:
            print("Something went wrong when performing a request")
            raise
        if not response._content.success:
            print("Wrong request parameters.")
            raise Exception("Wrong request parameters.")
        return response._content.result


class Money(object):
    DEFAULT_CURRENCY = "BYR"

    def __init__(self, amount=0, currency=DEFAULT_CURRENCY):
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, (float, int, Decimal)):
            raise Exception("The value should be numeric.")
        self._amount = Decimal(value)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if value not in CURRENCIES_CODES:
            raise Exception("The currency code is invalid.")
        self._currency = value

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.currency == other.currency:
                value = self.amount + other.amount
            else:
                value = self.amount + CurrencyConverter.convert(
                    other.amount, other.currency, self.currency
                )
            return Money(value, self.currency)
        elif isinstance(other, (float, int, Decimal)):
            return Money(self.amount + Decimal(other), self.currency)
        else:
            raise TypeError(self.UNSUPPORTED_OPERATION.format(
                "+", self.__class__, type(other)
            ))

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            if self.currency == other.currency:
                self.amount += other.amount
            else:
                self.amount += CurrencyConverter.convert(
                    other.amount, other.currency, self.currency
                )
        elif isinstance(other, (float, int, Decimal)):
            self.amount += Decimal(other)
        else:
            raise TypeError(self.UNSUPPORTED_OPERATION.format(
                "+=", self.__class__, type(other)
            ))

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if self.currency == other.currency:
                value = self.amount * other.amount
            else:
                value = self.amount * CurrencyConverter.convert(
                    other.amount, other.currency, self.currency
                )
            return Money(value, self.currency)
        elif isinstance(other, (float, int, Decimal)):
            return Money(self.amount * Decimal(other), self.currency)
        else:
            raise TypeError(self.UNSUPPORTED_OPERATION.format(
                "*", self.__class__, type(other)
            ))

    def __imul__(self, other):
        if isinstance(other, self.__class__):
            if self.currency == other.currency:
                self.amount *= other.amount
            else:
                self.amount *= CurrencyConverter.convert(
                    other.amount, other.currency, self.currency
                )
        elif isinstance(other, (float, int, Decimal)):
            self.amount *= Decimal(other)
        else:
            raise TypeError(self.UNSUPPORTED_OPERATION.format(
                "*=", self.__class__, type(other)
            ))

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            if self.currency == other.currency:
                value = self.amount / other.amount
            else:
                value = self.amount / CurrencyConverter.convert(
                    other.amount, other.currency, self.currency
                )
            return Money(value, self.currency)
        elif isinstance(other, (float, int, Decimal)):
            return Money(self.amount / Decimal(other), self.currency)
        else:
            raise TypeError(self.UNSUPPORTED_OPERATION.format(
                "/", self.__class__, type(other)
            ))

    def __idiv__(self, other):
        if isinstance(other, self.__class__):
            if self.currency == other.currency:
                self.amount /= other.amount
            else:
                self.amount /= CurrencyConverter.convert(
                    other.amount, other.currency, self.currency
                )
        elif isinstance(other, (float, int, Decimal)):
            self.amount /= Decimal(other)
        else:
            raise TypeError(self.UNSUPPORTED_OPERATION.format(
                "/=", self.__class__, type(other)
            ))

    def __neg__(self):
        self.amount = -self.amount
        return self

    def __sub__(self, other):
        return self.__add__(-other)

    def __isub__(self, other):
        self.__iadd__(-other)

    def __str__(self):
        return "{} {}".format(self.amount, self.currency)
