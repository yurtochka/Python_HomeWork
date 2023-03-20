# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import os

os.system('cls')
amount = int(input('Enter the sum of the number: '))
product = int(input('Enter the number of the product: '))
for i in range(amount):
    for j in range(product):
        if (amount == i + j) and (product == i * j):
            print(f'{amount} = {i} + {j}')
            print(f'{product} = {i} * {j}')
