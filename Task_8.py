# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n_slice = int(input('Enter the number of slices in length: '))
m_slice = int(input('Enter the number of slices in weight: '))
k_slice_break = int(input('Enter the number of slices you want to break off: '))
if ((k_slice_break % n_slice == 0) or (k_slice_break % m_slice == 0)) and (k_slice_break < n_slice * m_slice):
    print(f'{n_slice} {m_slice} {k_slice_break} -> yes')
else:
    print(f'{n_slice} {m_slice} {k_slice_break} -> no')