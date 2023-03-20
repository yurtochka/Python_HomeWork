# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os

os.system('cls')

number = int(input('Enter number: '))
degree = 1
while number >= degree:
    print(degree, end=' ')
    degree = degree * 2
