# 5_2

nums_generator = (number for number in range(1, int(input('Введите целое число: ')) + 1, 2))
print(*nums_generator)
print(next(nums_generator))
