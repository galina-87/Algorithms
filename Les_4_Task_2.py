# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и
# сложность алгоритмов.
import timeit
import cProfile
import math

# Test:
def test(func):
    z = [2, 3, 5, 7, 11, 13, 17,	19,	23,	29,	31,	37, 41,	43,	47,	53,	59,	61, 67,	71,	73,	79,	83,	89,
         97, 101,	103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
         193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
         307,  311, 313, 317, 331, 337, 347, 349, 353, 359,  367, 373, 379, 383, 389, 397, 401, 409,
         419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
    for i in range(0, 100):
        if z[i] == func(i+1):
            print(f'Test {i} OK')
        else:
            print('Ошибочное значение!')


# Решето Эратосфена:
def sieve_of_Eratosthenes(n):
    if n == 1:
        res = 2
    else:
        x = 2
        while x/math.log(x) < n+1:
            x += 1
        sieve = [i for i in range(x)]
        # print(sieve)
        sieve[1] = 0
        for i in range(2, x):
            if sieve[i] != 0:
                j = i + i
                while j < x:
                    sieve[j] = 0
                    j += i

        # print(sieve)
        res_1 = [i for i in sieve if i != 0]
        res = res_1[n-1]
    return (res)

# test(sieve_of_Eratosthenes)

# Простой перебор:
# Вспомогательная функция, возвращает 1, если на вход подано простое число и 0 - если подано составное число
# (предполагается, что числа меньше 2 на вход не могут попасть)
def prost(d):
    flag = 1
    for i in range(2, d):
        if d % i == 0:
            flag = 0

    return (flag)

# Простой перебор чисел последовательно, если число оказывается простым,
# то x - порядковый номер простого числа увеличивается на 1
def simple_iteration(n):
    x = 1
    rez = 2
    while x != n:
        rez += 1
        if prost(rez):
            x += 1

    return (rez)


# test(simple_iteration)
print(timeit.timeit('sieve_of_Eratosthenes(5)', number=1000, globals=globals()))   # 0.021020200000000003
print(timeit.timeit('sieve_of_Eratosthenes(10)', number=1000, globals=globals()))  # 0.0451169
print(timeit.timeit('sieve_of_Eratosthenes(20)', number=1000, globals=globals()))  # 0.1038962
print(timeit.timeit('sieve_of_Eratosthenes(40)', number=1000, globals=globals()))  # 0.24777910000000003
print(timeit.timeit('sieve_of_Eratosthenes(80)', number=1000, globals=globals()))  # 0.6786850999999999

cProfile.run('sieve_of_Eratosthenes(5)')   # 16    0.000    0.000    0.000    0.000 {built-in method math.log}
cProfile.run('sieve_of_Eratosthenes(10)')  # 40    0.000    0.000    0.000    0.000 {built-in method math.log}
cProfile.run('sieve_of_Eratosthenes(20)')  # 95    0.000    0.000    0.000    0.000 {built-in method math.log}
cProfile.run('sieve_of_Eratosthenes(40)')  # 221    0.000    0.000    0.000    0.000 {built-in method math.log}


print(timeit.timeit('simple_iteration(5)', number=1000, globals=globals()))   # 0.017944500000000002
print(timeit.timeit('simple_iteration(10)', number=1000, globals=globals()))  # 0.12614599999999998
print(timeit.timeit('simple_iteration(20)', number=1000, globals=globals()))  # 0.3821801
print(timeit.timeit('simple_iteration(40)', number=1000, globals=globals()))  # 1.970326
print(timeit.timeit('simple_iteration(80)', number=1000, globals=globals()))  # 10.6160605

cProfile.run('simple_iteration(5)')   # 9    0.000    0.000    0.000    0.000 Les_4_Task_2.py:51(prost)
cProfile.run('simple_iteration(10)')  # 27    0.000    0.000    0.000    0.000 Les_4_Task_2.py:51(prost)
cProfile.run('simple_iteration(20)')  # 69    0.000    0.000    0.000    0.000 Les_4_Task_2.py:51(prost)
cProfile.run('simple_iteration(40)')  # 171    0.002    0.000    0.002    0.000 Les_4_Task_2.py:51(prost)

# Краткий анализ:
# Алгориптм с использоватнием "Решета Эратосфена" оказался выгоднее простого перебора по времени - при увеличении входных
# данных в два раза время исполнение растет примерно в два раза - то есть зависимость линейная О(n). Время выполнения
# функции с простым перебором значений росло с ростом входных данных в 2 заза примерно в 9-10 раз, что говорит так же о
# линейной зависимости, но соотношение О(5n). Судя по количеству вызываемых вспомогательных функций ("Решето" вызывает
# функцию log() из модуля math в соотношении 1:3,5, в свою очередь простой перебор вызывает вспомогательную функцию -
# prost() в соотношении к входным данным примерно 1:2,5.
# Графики зависимостей времени от входных данных можно посмотреть по ссылке:
# https://drive.google.com/file/d/1VlumpDprJg3L75Kloa8zWcEo73vC2hLy/view?usp=sharing