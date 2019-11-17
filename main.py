from functions import *

years = int(input("Срок размещения капитала (лет): "))
initial_capital = float(input("Начальный капитал ($): "))
percent = float(input("Процентная ставка (%/мес.): "))
investment_infusion = float(input("Инвестиционные вливания ($/мес.): "))

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

capital = initial_capital
for year in range(years):
    print('\n{} год'.format(year + 1))
    print('-' * 60)
    for month in months:
        init_cap = capital
        percs = capital * percent/100
        capital += percs

        print_block(str(month), 10)
        str_init = '{:,.2f}'.format(init_cap).replace(',', ' ')
        print_block(str_init, 15)
        str_percs = '{:,.2f}'.format(percs).replace(',', ' ')
        print_block(str_percs, 10)
        str_cap = '{:,.2f}'.format(capital).replace(',', ' ')
        print_block(str_cap, 15, end='|\n')
        capital += investment_infusion
    print('-' * 60)
