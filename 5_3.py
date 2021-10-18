# 5_3
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = (user_tuples for user_tuples in zip_longest(tutors, klasses))

print(type(result))
print(*result)
print(next(result))
