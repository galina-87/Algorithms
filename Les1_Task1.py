# https://drive.google.com/file/d/1zIIiau3huXO3s31cDYRp3acX-GTYNpN4/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
print('Введите трехзначное число')
a = int(input())
P = 1
Sum = 0
P = a% 10
Sum = a % 10
a = a // 10
P *= a% 10
Sum += a % 10
a = a // 10
P *= a% 10
Sum += a % 10
a = a // 10
print('Произведение цифр: ', P, ' Сумма цифр: ', Sum)