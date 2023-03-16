# Найдите сумму цифр трехзначного числа.
# *Пример:* 123 -> 6 (1 + 2 + 3) 100 -> 1 (1 + 0 + 0) |


three_dig_num = int(input('input three-digit numbers: '))
print()
sum_num = 0
sum_num1 = 0
sum_num1 = three_dig_num % 10
print(sum_num1)
three_dig_num = three_dig_num // 10
sum_num = sum_num + sum_num1
print('+')
sum_num1 = three_dig_num % 10
print(sum_num1)
three_dig_num = three_dig_num // 10
sum_num = sum_num + sum_num1
print('+')
sum_num1 = three_dig_num % 10
print(sum_num1)
sum_num = sum_num + sum_num1

print('=')
print(sum_num)
