years = int(input("Срок размещения капитала (лет):"))
initial_capital = float(input("Начальный капитал ($):"))
percent = float(input("Процентная ставка (%/мес.):"))
investment_infusion = float(input("Инвестиционные вливания ($/мес.):"))

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

capital = initial_capital
for year in range(years):
    print('{} год'.format(year + 1))
    for month in months:
        init_cap = capital
        percs = capital * percent/100
        capital += percs
        print('\t{}   {:,.2f}    {:,.2f}    {:,.2f}'.format(month, init_cap, percs, capital).replace(',', ' '))
        capital += investment_infusion
