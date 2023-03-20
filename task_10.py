# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import os

os.system('cls')  # clearing the screen

from random import randint

count_coins = int(input('Enter count of coins: '))
print()
coins = 0
eagle = 0
tails = 0
while count_coins >= coins:
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp == 0:
        eagle += 1
    else:
        tails += 1
    coins += 1
if eagle > tails:
    print(f'\nMin number of coins to flip -> {tails}')
else:
    print(f'\nMin number of coins to flip -> {eagle}')
