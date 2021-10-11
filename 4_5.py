
from utils import currency_rates
from sys import argv


print(currency_rates('usD'))
print(currency_rates('EuR'))
print(currency_rates('AZN'))
print(currency_rates('BGN'))
print(currency_rates('AMD'))
print(currency_rates('CHF'))
print(currency_rates('CNY'))
_, n = argv
print(currency_rates(n))
