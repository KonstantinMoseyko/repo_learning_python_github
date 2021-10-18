#  5_5
# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# ver_1
result = [ind for ind in src if src.count(ind) == 1]
print(result)

# ver_2
unique_digits = set()
comparison_digits = set()
for ind in src:
    if ind not in comparison_digits:
        unique_digits.add(ind)
    else:
        unique_digits.discard(ind)
    comparison_digits.add(ind)
result = [ind for ind in src if ind in unique_digits]
print(result)
