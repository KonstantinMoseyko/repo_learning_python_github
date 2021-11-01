class Stationery:
    def __init__(self, title='непонятным предметом'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандошом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')


stat_draw = Stationery()
pen = Pen('BIC')
pencil = Pencil('KOH-I-NOOR')
marker = Handle('Attache')

pandora_box = [stat_draw, pen, pencil, marker]
for val in pandora_box:
    val.draw()
