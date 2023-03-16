# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
# 385916 -> yes
# 123456 -> no

number_ticket = int(input('Enter number ticket: '))
number_ticket1 = 0
sum_nt1 = 0
number_ticket2 = 0
sum_nt2 = 0
number_ticket1 = number_ticket // 1000
number_ticket2 = number_ticket % 1000
sum_nt1 = ((number_ticket1 % 10) + ((number_ticket1 % 100) // 10) + (number_ticket1 // 100))
sum_nt2 = ((number_ticket2 % 10) + ((number_ticket2 % 100) // 10) + (number_ticket2 // 100))
if sum_nt1 == sum_nt2:
    print(f'{number_ticket} -> yes')
else:
    print(f'{number_ticket} -> no')
