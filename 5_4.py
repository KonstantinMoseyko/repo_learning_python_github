# 5_4
# result = [12, 44, 4, 10, 78, 123]
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[index] for index in range(1, len(src)) if src[index] > src[index - 1]]
print(result)
