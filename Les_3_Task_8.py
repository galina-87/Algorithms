# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в последнюю ячейку строки. В конце следует вывести полученную матрицу.

import random

SIZE_1 = 5
SIZE_2 = 4
MIN_ITEM = 0
MAX_ITEM = 10
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)] for _ in range(SIZE_1)]
print('Исходная матрица: ')
print(*matrix, sep='\n')

for i in range(SIZE_1):
    sum_ = 0
    for j in range(SIZE_2):
        sum_ = sum_ + matrix[i][j]
    matrix[i].append(sum_)

print('Матрица с добавленным элементов в каждую строчку - суммой предыдущих элементов: ')
print(*matrix, sep='\n')