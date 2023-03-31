# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

size_list = int(input('Enter size of the list: '))
random_list = [randint(1, 20) for i in range(size_list)]
print(random_list)
min_num, max_num = list(
    map(int, input('Enter the min and max elements of the list separated in the space: ').split(' ')))
count_index_list = [i for i in range(len(random_list)) if (min_num <= random_list[i] <= max_num)]
print(count_index_list)
