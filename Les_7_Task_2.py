# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    rez = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            rez.append(left[0])
            left = left[1:]
        else:
            rez.append(right[0])
            right = right[1:]
    if len(left) > 0:
        rez += left
    if len(right) > 0:
        rez += right
    print(rez)
    return rez



SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randrange(MIN_ITEM, MAX_ITEM) + random.random() for _ in range(SIZE)]
print(f'Неотсортированный массив: \n{array}')
print((f'Отсортированный массив:   \n{merge_sort(array)}'))