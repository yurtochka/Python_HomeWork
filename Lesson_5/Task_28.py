# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Пример:*
# 2 2
#  4

first_num, second_num = list(map(int, input('Enter two numbers separated by a space: ').split(' ')))

sum_num = lambda num1, num2: num1 if num2 == 0 else sum_num(num1 + 1, num2 - 1)

res_sum = sum_num(first_num, second_num)
print(f'result -> {res_sum}')
