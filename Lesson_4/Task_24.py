# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.


from random import randint

number_of_bushes = int(input('Enter the number of bushes: '))
number_of_berries = [randint(10, 100) for _ in range(number_of_bushes)]
print(number_of_berries)
temp = 0
for i in range(number_of_bushes):

    if i == 1:
        res = number_of_berries[0] + number_of_berries[1] + number_of_berries[-1]
    elif i == len(number_of_berries):
        res = number_of_berries[-2] + number_of_berries[-1] + number_of_berries[0]
    else:
        res = number_of_berries[i-1] + number_of_berries[i-2] + number_of_berries[i]
    if res > temp:
        temp = res
print(temp)

