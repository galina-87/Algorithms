# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

# функция, считающая сумму двух 16-ричных чисел
def sum_16(a, b):
    cyf_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    mas_1 = []
    for i in range(len(a)):
        mas_1.append(a[i])

    mas_2 = []
    for i in range(len(b)):
        mas_2.append(b[i])

    if len(a) > len(b):
        mlen = len(a)
        for i in range(len(a) - len(b)):
            mas_2.insert(0, '0')
    else:
        mlen = len(b)
        for i in range(len(b) - len(a)):
            mas_1.insert(0, '0')

    rez = deque()
    temp = 0
    while mlen > 0:
        temp_1 = (temp + cyf_.index(str(mas_1[mlen-1])) + cyf_.index(str(mas_2[mlen-1]))) % 16
        rez.appendleft(cyf_[temp_1])
        temp = (temp + cyf_.index(str(mas_1[mlen-1])) + cyf_.index(str(mas_2[mlen-1]))) // 16
        mlen -= 1

    if temp > 0:
        rez.appendleft(cyf_[temp])

    return (rez)

# функция, считающая произведение двух 16-ричных чисел
# Решила использовать то, что уже есть, а именно - функцию суммы:
def pr_16(x, y):
    cyf_0 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    k = 0
    rez_1 = ''
    for i in reversed(y):
        z = x
        for j in range(cyf_0.index(i) - 1):
            z = str(''.join(sum_16(z,x)))
        z = z + '0'*k
        rez_1 = str(''.join(sum_16(rez_1,z)))
        k += 1
    return list(rez_1)


# программа, вычисляющая сумму и произведение двух 16-ричных чисел
a0 = str(input('Введите первое 16-ричное число: '))
b0 = str(input('Введите второе 16-ричное число: '))
a0 = a0.upper()
b0 = b0.upper()

print(sum_16(a0, b0))
print(pr_16(a0, b0))


