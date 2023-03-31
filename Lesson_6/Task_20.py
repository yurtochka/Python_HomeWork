# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


first_element, difference, number_elements = list(
    map(int, input('enter three parameters separated by a space: ').split(' ')))

res = [(first_element + (i * number_elements)) for i in range(number_elements)]
print(res)
