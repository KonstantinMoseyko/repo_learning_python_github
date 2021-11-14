class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите делитель - число не равное нулю: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise OwnError("Вы ввели ноль, на ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data}")

