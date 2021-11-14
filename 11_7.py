class Cmplx:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y

    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y


x = float(input())
y = float(input())
a = Cmplx(x, y)
x = float(input())
y = float(input())
b = Cmplx(x, y)
a + b
a * b
print(f'Сумма:   {a.sumax:.2f} + {a.sumay:.2f}j')
print(f'Произв.: {a.multx:.2f} + {a.multy:.2f}j')
