# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Ищет крайние левые максимальный и минимальный элементы

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = array[0]
max_ = array[0]
imin = 0
imax = 0

for i in range(SIZE):
    if array[i] < min_:
        min_ = array[i]
        imin = i
    if array[i] > max_:
        max_ = array[i]
        imax = i

array[imax] = min_
array[imin] = max_

print(array)