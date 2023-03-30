# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def sqrt_recur(number, degree):
    if degree == 1:
        return number
    else:
        return number * sqrt_recur(number, degree - 1)


num = int(input('Enter number: '))
deg = int(input('Enter degree: '))
print(f'Number {num} in the degree {deg} -> {sqrt_recur(num, deg)}')
