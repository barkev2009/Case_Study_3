from functions import *

years = int(input("Срок размещения капитала (лет): "))
initial_capital = float(input("Начальный капитал ($): "))
percent = float(input("Процентная ставка (%/мес.): "))
investment_infusion = float(input("Инвестиционные вливания ($/мес.): "))

maxes = get_maxes(years, initial_capital, percent, investment_infusion)

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

# Setting design elements
dashes = '-' * (9 + max(maxes['months'], count_symbols(' месяц '))
                + max(maxes['init_cap'], count_symbols(' инвестиций '))
                + max(maxes['percs'], count_symbols(' сумма, % '))
                + max(maxes['capital'], count_symbols(' капитал ')))
month_block_width = max(maxes['months'], count_symbols(' месяц '))
init_block_width = max(maxes['init_cap'], count_symbols(' инвестиций '))
per_block_width = max(maxes['percs'], count_symbols(' сумма, % '))
cap_block_width = max(maxes['capital'], count_symbols(' капитал '))

capital = initial_capital
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
        init_cap = capital
        percs = capital * percent / 100
        capital += percs

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
