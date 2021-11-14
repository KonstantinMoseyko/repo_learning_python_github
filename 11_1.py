class Data:
    def init(self, data):
        self.data = data  # создаем  атрибут класса в конструкторе
        # и ссылку на объект

    @classmethod
    def mod(cls, ds):
        d, m, y = map(int, ds.split('-'))  # задаем classmethod  cls,
        # мапим с int и распаковываем в 3 переменых

        cls.validation(d, m, y)  # для класса вызываем метод  validation(staticmethod)
        return cls.validation(d, m, y)  # возвращаем итоговый результат

    @staticmethod
    def validation(d, m, y):

        if d < 31 and m < 12 and y < 1999:  # получаем парпметры для валидации
            return f'День {d} Месяц {m}  Год {y}'  # возвращаем строку
        else:
            return 'Некорректная дата'


data_1 = Data.mod('12-2-1988')
print(data_1)
data_2 = Data.mod('12-32-1988')
print(data_2)
