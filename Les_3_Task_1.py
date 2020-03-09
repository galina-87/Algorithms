# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
MIN_ITEM = 2
MAX_ITEM =  99
MIN_DIV = 2
MAX_DIV = 9

array = [_ for _ in range(MIN_ITEM, MAX_ITEM+1)]
print(array)

array_1 = [0 for _ in range(MIN_DIV, MAX_DIV+1)]
# print(array_1)

for i in range(0, len(array)):
    for j in range(MIN_DIV, MAX_DIV+1):
        if array[i] % j == 0:
            array_1[j-MIN_DIV] += 1

# Вывод количества чисел, кратных каждому из чисел от  заданного начального (2) до заданного раненн конечного (9)
print(array_1)



