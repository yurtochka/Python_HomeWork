# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint

first_num = int(input('Enter count element first set: '))
my_list1 = [randint(1, 20) for _ in range(first_num)]
print(my_list1)
second_num = int(input('Enter count element second set: '))
my_list2 = [randint(1, 20) for _ in range(second_num)]
print(my_list2)
print()
print(sorted(set(my_list1).intersection(set(my_list2))))
