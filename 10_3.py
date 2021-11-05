class Cell:
    def __init__(self, user_num):
        self.user_num = user_num

    def __str__(self):
        return f"{self.user_num}"

    def __add__(self, other):
        return Cell(self.user_num + other.user_num)

    def __sub__(self, other):
        return Cell(self.user_num - other.user_num) if self.user_num - other.user_num > 0 \
            else "Разность количества ячеек двух клеток меньше нуля"

    def __mul__(self, other):
        return Cell(self.user_num * other.user_num)

    def __floordiv__(self, other):
        return Cell(self.user_num // other.user_num)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.user_num // rows)]) + "\n" + ('*' * (self.user_num % rows))


cell_num1 = Cell(31)
cell_num2 = Cell(27)
print(cell_num1 + cell_num2)
print(cell_num1 - cell_num2)
print(cell_num1 * cell_num2)
print(cell_num1 // cell_num2)
print(cell_num1.make_order(5))
