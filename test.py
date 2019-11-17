from numpy import *
ending = 5000*1.1
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']


# print(count_nonzero(list(month.replace(' ', '1'))))
mon_lists = []
for month in months:
    mon_lists.append(2 + count_nonzero(list(month)))

print(mon_lists)