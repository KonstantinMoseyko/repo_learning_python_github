class Warehouse:
    def __init__(self, *subjects):
        self.subjects = {k: [] for k in subjects}

    def __str__(self):
        return f'Cписок поступлений: {self.subjects}'

    def my_list(self):
        return self.subjects

    def valid_printers(self):
        if len(self.subjects['Printer']) > 0:
            return f'Все хорошо, принтеры поступают на склад'
        else:
            return f'Внимание! Заявка на принтеры сформирована не правильно!'\
                   f'Обратитесь к своему менеджеру.'

    def valid_scanes(self):
        if len(self.subjects['Scanner']) > 0:
            return f'Все хорошо, сканеры поступают на склад'
        else:
            return f'Внимание! Заявка на сканеры сформирована не правильно!'\
                   f' Обратитесь к своему менеджеру.'

    def valid_xerox(self):
        if len(self.subjects['Xerox']) > 0:
            return f'Все хорошо, ксероксы поступают на склад'
        else:
            return f'Внимание! Заявка на ксероксы сформирована не правильно!'\
                   f' Обратитесь к своему менеджеру.'


class OfficeEquipment:
    def __init__(self, name, types):
        self.name = name
        self.types = types


class Scaner(OfficeEquipment):
    def __init__(self, name, types="Scanner"):
        super().__init__(name, types)


class Printer(OfficeEquipment):
    def __init__(self, name, types="Printer"):
        super().__init__(name, types)


class Xerox(OfficeEquipment):
    def __init__(self, name, types="Xerox"):
        super().__init__(name, types)


storage = Warehouse('Scanner', 'Printer', 'Xerox')
p_1 = Printer('HP')
p_2 = Printer('Brother')
p_3 = Printer('Samsung')
p_4 = Printer('Canon')
s_1 = Scaner('Honeywell')
storage.subjects[p_1.types].append(p_1.name)
storage.subjects[p_2.types].append(p_2.name)
storage.subjects[p_3.types].append(p_3.name)
storage.subjects[p_4.types].append(p_4.name)
storage.subjects[s_1.types].append(s_1.name)
print(storage)
print(storage.valid_printers())
print(storage.valid_scanes())
print(storage.valid_xerox())
