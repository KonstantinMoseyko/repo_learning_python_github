class Matrix:
    def __init__(self, user_matrix):
        self.user_matrix = user_matrix

    def __str__(self):
        return f"{str(self.user_matrix[0]).strip('[]').replace(',', ' ')}\n" \
               f"{str(self.user_matrix[1]).strip('[]').replace(',', ' ')}\n" \
               f"{str(self.user_matrix[2]).strip('[]').replace(',', ' ')}\n"

    def __add__(self, other):
        matrix_sum = [[cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
                      for row_1, row_2 in zip(self.user_matrix, other.user_matrix)]
        return Matrix(matrix_sum)


matrix_num1 = Matrix([[2, 2, 2], [3, 3, 3], [4, 4, 4]])
matrix_num2 = Matrix([[5, 5, 5], [6, 6, 6], [7, 7, 7]])
print(matrix_num1)
print(matrix_num1 + matrix_num2)
