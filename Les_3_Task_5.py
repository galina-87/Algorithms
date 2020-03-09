# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = MIN_ITEM - 1
imax = -1

for i in range(SIZE):
    if (array[i] < 0) and (array[i] > max_):
        max_ = array[i]
        imax = i

if max_ == MIN_ITEM - 1:
    print ('Отрицательных элементов в массиве нет')
else:
    print(f'{max_:>5}', ' - значение')
    print(f'{imax:>5}', ' - позиция')