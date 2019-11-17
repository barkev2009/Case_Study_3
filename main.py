from functions import *

years = int(input("Срок размещения капитала (лет): "))
initial_capital = float(input("Начальный капитал ($): "))
percent = float(input("Процентная ставка (%/мес.): "))
investment_infusion = float(input("Инвестиционные вливания ($/мес.): "))

maxes = get_maxes(years, initial_capital, percent, investment_infusion)

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

capital = initial_capital
for year in range(years):
    print('\n{} год'.format(year + 1))
    print('-' * (9 + max(maxes['months'], count_symbols(' месяц '))
                 + max(maxes['init_cap'], count_symbols(' инвестиций '))
                 + max(maxes['percs'], count_symbols(' сумма, % '))
                 + max(maxes['capital'], count_symbols(' капитал '))))
    print_block(' ', max(maxes['months'], count_symbols(' месяц ')))
    print_block(' основа ', max(maxes['init_cap'], count_symbols(' инвестиций ')))
    print_block(' сумма, % ', max(maxes['percs'], count_symbols(' сумма, % ')))
    print_block(' ', max(maxes['capital'], count_symbols(' капитал ')), end='|\n')
    print_block(' месяц ', max(maxes['months'], count_symbols(' месяц ')))
    print_block(' инвестиций ', max(maxes['init_cap'], count_symbols(' инвестиций ')))
    print_block(' за месяц ', max(maxes['percs'], count_symbols(' сумма, % ')))
    print_block(' капитал ', max(maxes['capital'], count_symbols(' капитал ')), end='|\n')
    print('-' * (9 + maxes['months'] + maxes['init_cap'] + maxes['percs'] + maxes['capital']))

    for month in months:
        init_cap = capital
        percs = capital * percent/100
        capital += percs

        print_block(str(month), max(maxes['months'], count_symbols(' месяц ')))
        str_init = '{:,.2f}'.format(init_cap).replace(',', ' ')
        print_block(str_init, max(maxes['init_cap'], count_symbols(' инвестиций ')))
        str_percs = '{:,.2f}'.format(percs).replace(',', ' ')
        print_block(str_percs, max(maxes['percs'], count_symbols(' сумма, % ')))
        str_cap = '{:,.2f}'.format(capital).replace(',', ' ')
        print_block(str_cap, max(maxes['capital'], count_symbols(' капитал ')), end='|\n')
        capital += investment_infusion
    print('-' * (9 + maxes['months'] + maxes['init_cap'] + maxes['capital'] + maxes['percs']))
