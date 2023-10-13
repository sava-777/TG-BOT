import requests

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        if base == quote:
            raise APIException("Нельзя конвертировать одну и ту же валюту.")

        url = f"https://api.coingate.com/v2/rates/merchant/{base}/{quote}"
        response = requests.get(url)

        if response.status_code != 200:
            raise APIException("Ошибка при запросе к API.")

        rate = response.content.decode("utf-8")

        try:
            rate = float(rate)
        except ValueError:
            pass

        if isinstance(rate, float):
            return float(rate) * float(amount)
        else:
            raise APIException("Ошибка при обработке курса.")
        raise ConvertException(f'Не удалось обработать количество {amount}') 
    
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    total_base = json.loads(r.content)[keys[base]]
    return total_base
