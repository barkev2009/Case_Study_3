from functions import *
from matplotlib.pyplot import *

years = int(while_print('Срок размещения капитала (лет): ', 'Некорректный ввод, попробуйте еще раз!'))
initial_capital = float(while_print('Начальный капитал ($): ', 'Некорректный ввод, попробуйте еще раз!'))
percent = float(while_print('Процентная ставка (%/мес.): ', 'Некорректный ввод, попробуйте еще раз!'))
investment_infusion = float(while_print('Инвестиционные вливания ($/мес.): ',
                                        'Некорректный ввод, попробуйте еще раз!'))

maxes = get_maxes(years, initial_capital, percent, investment_infusion)

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

# Setting design elements
month_block_width = max(maxes['months'], count_symbols(' месяц '))
init_block_width = max(maxes['init_cap'], count_symbols(' инвестиций '))
per_block_width = max(maxes['percs'], count_symbols(' сумма, % '))
cap_block_width = max(maxes['capital'], count_symbols(' капитал '))
dashes = '-' * (9 + month_block_width + init_block_width + per_block_width + cap_block_width)


capital = initial_capital
x_vector = []
y_vector = []
for year in range(years):

    # Header
    print('\n{} год'.format(year + 1))

    print(dashes)
    print_block(' ', month_block_width)
    print_block(' основа ', init_block_width)
    print_block(' сумма, % ', per_block_width)
    print_block(' ', cap_block_width, end='|\n')

    print_block(' месяц ', month_block_width)
    print_block(' инвестиций ', init_block_width)
    print_block(' за месяц ', per_block_width)
    print_block(' капитал ', cap_block_width, end='|\n')

    print(dashes)

    for month in months:
        x_vector.append('{} {}'.format(year, month))
        init_cap = capital
        percs = capital * percent / 100
        capital += percs
        y_vector.append(capital)

        # Main body
        print_block(str(month), month_block_width)
        str_init = '{:,.2f}'.format(init_cap).replace(',', ' ')
        print_block(str_init, init_block_width)
        str_percs = '{:,.2f}'.format(percs).replace(',', ' ')
        print_block(str_percs, per_block_width)
        str_cap = '{:,.2f}'.format(capital).replace(',', ' ')
        print_block(str_cap, cap_block_width, end='|\n')
        capital += investment_infusion
    print(dashes)

# Plotting the capital growth
fig, ax = subplots()
ax.plot(x_vector, y_vector)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('Время ->')
ax.set_ylabel('Капитал ->')
ax.set_title('Рост капитала с течением времени', fontsize=15)
show()
