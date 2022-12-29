# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 6782 -> 23 /// - 0,56 -> 11

value = input('Введите вещественное число: ')
summ = 0
for el in value:
    if el.isdigit():
        summ+=int(el)
print(summ)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.\
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N: '))
result = 1
for el in range (1, n):
    result *= el 
    print(result, end=", ")
print (n*result)

# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# Пример: -Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} => Сумма 9.06

n = int(input(('Задайте список из N чисел: ')))
dict = {}
summ = 0
for el in range(1, n+1):    
    dict[el] = round((1 + 1/el) ** el, 2)
    summ += dict[el]
print(f'Для n={n} {dict} => Сумма {round(summ, 2)} ')

# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите количество элементов списка: '))
list = []
from random import randint
for i in range(1, n + 1):    
    list.append(randint(1,100))
print(list)
random.shuffle(list)
print(list)

