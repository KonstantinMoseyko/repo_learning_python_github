class Digit(Exception):
    def init(self, txt):
        self.txt = txt


flag = 'ДА'
listing = []

while flag == 'ДА':
    try:
        n = input('Введит целое число')
        if int(n) < 0:
            raise Digit("Вы ввели не позитивное число!!!")
            flag = input('Вы хотите продолжить нажмите ДА')
    except ValueError:
        print("Вы ввели не число!")
        flag = input('Ва хотите продолжить  ДА  или НЕТ')
    except Digit as err:
        print(err)
        flag = input('Ва хотите продолжить  ДА  или НЕТ')
    else:
        listing.append(n)
        print('добавленно в список')
print(f"Ваш список: {listing}")
