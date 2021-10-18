# 5_1

def nums_generator(user_num):
    for number in range(1, user_num+1, 2):
        yield number


user_gen = nums_generator(int(input('Введите целое число: ')))
for ind in user_gen:
    print(ind)

print(next(user_gen))
