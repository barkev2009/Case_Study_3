years = int(input("Срок размещения капитала (лет):"))
initial_capital = float(input("Начальный капитал ($):"))
percent = float(input("Процентная ставка (%/мес.):"))
investment_infusion = float(input("Инвестиционные вливания ($/мес.):"))

months = range(1, 13)

capital = initial_capital
for year in range(years):
    for month in months:
        init_cap = capital
        percs = capital * percent
        capital += percs
        print('{:.2f} {:.2f} {:.2f}'.format(init_cap, percs, capital))
        capital += investment_infusion
