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
