# 2.	Написать функцию currency_rates(), принимающую в качестве аргумента
# код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.

from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(user_name_currency):
    """
    Функция принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
    и возвращающает курс этой валюты по отношению к рублю, дату.

    :param user_name_currency: код валюты (например, USD, EUR, GBP, ...)
    :return: курс валюты по отношению к рублю, дату
    """
    raw_list_of_currency = content.split('<Valute')
    correct_exchange_rate_dict = {}
    date = raw_list_of_currency[0][60:70]

    for ind in raw_list_of_currency[1:]:
        _trash1, result1, _trash2, _trash3, result2, *_trash_other = ind.split('</')
        name_currency = result1[18:]
        exchange_rate = float(result2[12:].replace(',', '.'))
        correct_exchange_rate_dict.setdefault(name_currency, exchange_rate)
    return correct_exchange_rate_dict.get(user_name_currency.upper()), date


print(currency_rates('usD'))
print(currency_rates('EuR'))
