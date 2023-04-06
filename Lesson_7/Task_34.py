# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод: Парам пам-пам


def poem(my_string):
    my_string = my_string.split()
    vowel_letters = list('ауоыиэяюёе')
    my_list = []
    for word in my_string:
        count_vowel = 0
        for i in word:
            if i in vowel_letters:
                count_vowel += 1
        my_list.append(count_vowel)
    return my_list


my_string_beat = input('Enter string poem, phrases is separated by a hyphen, words is separated by a space: ')
res_list = poem(my_string_beat)
if len(set(poem(my_string_beat))) == 1 and res_list[0] > 0:
    print('Парам пам-пам!')
else:
    print('Пам парам!')
