# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*#
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint
size_array = int(input('Enter size array: '))

my_list = [randint(1, 20) for _ in range(size_array)]
print(my_list)
nat_number = int(input('Enter natural number: '))
temp = abs(nat_number - my_list[0])
res = 0
for i in range(size_array - 1):
    if my_list[i] == nat_number:
        res = my_list[i]
        break
    temp1 = abs(nat_number - my_list[i])
    if temp > temp1:
        res = my_list[i]
        temp = temp1
print(f'the closest element to {nat_number} is {res}')