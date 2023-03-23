# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#  5
#  1 2 3 4 5
#  3
#  -> 1
from random import randint

size_array = int(input('Enter size array: '))

my_list = [randint(1, 20) for _ in range(size_array)]
print(my_list)
nat_number = int(input('Enter natural number: '))
temp = 0
for j in range(len(my_list)):
    if nat_number == my_list[j]:
        temp = temp + 1
print(f'Number {nat_number} occurs {temp} times')
