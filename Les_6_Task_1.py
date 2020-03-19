# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

# Решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Задача:
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from collections import deque
import random
import  sys

# Решение 1 - стандартное решение через цикл
def loop (ar):
    # print(ar)
    max_ = float('-inf')
    imax = -1
    for i in range(len(ar)):
        if (ar[i] < 0) and (ar[i] > max_):
            max_ = ar[i]
            imax = i

# Подсчет памяти в данном решении:
    var_ = locals()
    mem_ = 0
    for i in var_.keys():
        if i != 'mem_' and i != 'i':
            mem_ += sys.getsizeof(var_[i])
    mem_ += sys.getsizeof(var_) + sys.getsizeof(mem_) + sys.getsizeof(i)

    # проверка была - убирать совсем не буду - можно раскомментировать и проверить:
    # print(f'{sys.getsizeof(ar)} + {sys.getsizeof(max_)} + {sys.getsizeof(imax)} + {sys.getsizeof(mem_)} + {sys.getsizeof(i)}  +  {sys.getsizeof(var_)}')

    if max_ == float('-inf'):
        rez = f'Отрицательных элементов в массиве нет \nПамять под переменные {mem_} байт'
    else:
        rez = f'{max_:>5} - значение \n {imax:>5} - позиция \nПамять под переменные {mem_} байт'
    return (f'В алгоритме loop под переменные выделено {mem_} байт памяти')

# Решение 2 - решение через сортировкку: сначала массив сортируем, после чего просматриваем до первого неотрицательного
# элемента, если таковых нет, то до конца массива. Если находим неотрицательный элемент, то предыдущий - максимальный
# из отрицательных, если неотрицательного не нашли, то максимальный отрицателоьный элемент - последний.
def sort_List(ar):
    ar1 = sorted(ar)
    # print(ar1)
    i = 0
    while  (i < len(ar1)) and (ar1[i] < 0):
        i += 1

    if (i == 0) and (ar1[i] >= 0):
        rez = 'Отрицательных элементов в массиве нет'
    else:
        rez = f'значение = {ar1[i-1]} \nпозиция = {ar.index(ar1[i-1])}'

    # Подсчет памяти в данном решении ничем не отличается от передыдущего подсчета:
    var_ = locals()
    mem_ = 0
    for i in var_.keys():
        if i != 'mem_' and i != 'i':
            mem_ += sys.getsizeof(var_[i])
    mem_ += sys.getsizeof(var_) + sys.getsizeof(mem_) + sys.getsizeof(i)

    return (f'В алгоритме sort_List под переменные выделено {mem_} байт памяти')

# Решение 3 - суть заключается в том, что формируется новый массив - состоящий из отрицательных элементов анализируемого
# массива, к которорму затем применяется рекурсивная функция поиска максимума.

# Вот тут очень не уверена в подсчете памяти, но вроде похоже на правду - в глобальную переменную
# при каждом вызове рекурсии добавляем память которая выделилась при каждом последующем вызове на переменные,
# а в основной функции прибавляем эту память (из глобальной переменной) к той памяти, которая посчиталось в
# основной функции.

# Вспомогательная рекурсивная функция для поиска максимума в массиве
global mem
mem = 0
def rec_(m):
    global mem
    if len(m) == 1:
        mem += sys.getsizeof(m)
        return (m[0])
    else:
        max_ = m[len(m)-1]
        m.pop()
        mem += sys.getsizeof(max_) + sys.getsizeof(m)
        return(max(max_, rec_(m)))


def rec_1(ar): # функция поиска максимального отрицательного элемента, с помощью  рекурсивной функции поиска максимума
    global mem
    a = []
    for i in range(len(ar)):
        if (ar[i] < 0):
            a.append(ar[i])
    if a == []:
        rez = 'Отрицательных элементов в массиве нет'
    else:
        max_otr = rec_(a)
        rez = f'{max_otr:>5} - значение \n{ar.index(max_otr):>5} - позиция'
    # Подсчет памяти по основной функции:
    var_ = locals()
    mem_ = 0
    for i in var_.keys():
        if i != 'mem_' and i != 'i':
            mem_ += sys.getsizeof(var_[i])
    mem_ += sys.getsizeof(var_) + sys.getsizeof(mem_) + sys.getsizeof(i)
    # а на выход функции подаем сумму рекурсии и основной функций:
    return (f'В алгоритме rec_1, с учетом рекурсивной функции rec_ под переменные выделено {mem_ + mem} байт памяти')

# Программа
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = -1
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

print(loop(array))
print(sort_List(array))
print(rec_1(array))

# Версия интерпритатора: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
# ОС: Windows 10 Pro version 1903; 64-разрядная

# Для анализа были использовате несколько замеров со стандартными данными:
# SIZE = 10, MIN_ITEM = -100, MAX_ITEM = 100
# которые показали интересные результаты: у первого алгоритма сумма памяти для переменных не изменялась
# в зависимости от значений элементов массива, второй алгорим оказался средне зависим от количества отрицательных
# элементов в массиве, а рекурсия по испольуемой памяти оказалась весомо зависима от количества отрицательных
# элементов. Ниже приведены замеры с разными значениями объема памяти алгоритмов:

# [41, -4, -37, 40, -59, 26, 57, 69, -4, 79] - 4 отрицательных элемента
# В алгоритме loop под переменные выделено 550 байт памяти
# В алгоритме sort_List под переменные выделено 814 байт памяти
# В алгоритме rec_1, с учетом рекурсивной функции rec_ под переменные выделено 1192 байт памяти

# [-55, -99, -66, 28, 28, -67, -57, -64, -28, -18] - 8 отрицательных элементов
# В алгоритме loop под переменные выделено 550 байт памяти
# В алгоритме sort_List под переменные выделено 816 байт памяти
# В алгоритме rec_1, с учетом рекурсивной функции rec_ под переменные выделено 1808 байт памяти

# [-98, 28, 23, -46, -85, -52, -52, 89, 3, 63] - 5 отрицательных элементов
# В алгоритме loop под переменные выделено 550 байт памяти
# В алгоритме sort_List под переменные выделено 816 байт памяти
# В алгоритме rec_1, с учетом рекурсивной функции rec_ под переменные выделено 1364 байт памяти

# Для чистоты эксперимента использоватны массивы без отрицательных элементов:
# [5, 33, 11, 35, 95, 18, 63, 94, 93, 25]
# В алгоритме loop под переменные выделено 546 байт памяти
# В алгоритме sort_List под переменные выделено 836 байт памяти
# В алгоритме rec_1, с учетом рекурсивной функции rec_ под переменные выделено 700 байт памяти

# А так же, массивы состоящие только из отрицательных элементов:
# [-29, -61, -77, -100, -98, -85, -69, -25, -58, -98]
# В алгоритме loop под переменные выделено 550 байт памяти
# В алгоритме sort_List под переменные выделено 816 байт памяти
# В алгоритме rec_1, с учетом рекурсивной функции rec_ под переменные выделено 2280 байт памяти

# Общий вывод: минимальное количество памяти под переменные занимает первый алгоритм - loop, при этом объем
# используемой памяти не зависит от информации подаваемой на вход (то есть практически не зависит от того, какие
# элементы в массиве - отрицательные или положительные). Второй алгоритм - sort_List занимает в памяти больше места и
# он оказался зависим по памяти от того,  какого знака элементы во входящем массиве. Наиболее объемным является
# алгоритм с рекурсией, при этом он же наиболее зависим от знаков элементов входящего массива.