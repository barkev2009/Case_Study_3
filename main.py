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
    print('-' * (9 + maxes['months'] + maxes['init_cap'] + maxes['percs'] + maxes['capital']))
    print_block('       ', maxes['months'])
    print_block(' основа ', maxes['init_cap'])
    print_block(' сумма, % ', maxes['percs'])
    print_block('         ', maxes['capital'], end='|\n')
    print_block(' месяц ', maxes['months'])
    print_block(' инвестиций ', maxes['init_cap'])
    print_block(' за месяц ', maxes['percs'])
    print_block(' капитал ', maxes['capital'], end='|\n')
    print('-' * (9 + maxes['months'] + maxes['init_cap'] + maxes['percs'] + maxes['capital']))

    for month in months:
        init_cap = capital
        percs = capital * percent/100
        capital += percs

        print_block(str(month), maxes['months'])
        str_init = '{:,.2f}'.format(init_cap).replace(',', ' ')
        print_block(str_init, maxes['init_cap'])
        str_percs = '{:,.2f}'.format(percs).replace(',', ' ')
        print_block(str_percs, maxes['percs'])
        str_cap = '{:,.2f}'.format(capital).replace(',', ' ')
        print_block(str_cap, maxes['capital'], end='|\n')
        capital += investment_infusion
    print('-' * (9 + maxes['months'] + maxes['init_cap'] + maxes['capital'] + maxes['percs']))
