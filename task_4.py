# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1  4  1
# 24 -> 4  16  4


cranes_count = int(input('Enter the total numbers of cranes: '))
if (cranes_count % 3 == 0):
    cranes_katya = cranes_count // 3
    cranes_boys = cranes_katya // 2
    input(f'{cranes_count} -> {cranes_boys} {cranes_katya * 2} {cranes_boys}')
else:
    input('Entered data contradicts the condition of the task')
