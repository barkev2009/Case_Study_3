from numpy import count_nonzero as count_symbols


def print_block(obj, spaces, end=''):
    print('| {}'.format(obj), end='')
    print(' ' * (spaces - count_symbols(list(str(obj).replace(' ', '1')))), end=end)


def get_maxes(years, initial_capital, percent, investment_infusion):
    global init_cap, percs
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    mon_lists = []
    for month in months:
        mon_lists.append(2 + count_symbols(list(month)))

    capital = initial_capital
    for year in range(years):
        for month in months:
            init_cap = capital
            percs = capital * percent/100
            capital += percs
            capital += investment_infusion
    str_init = '{:,.2f} '.format(init_cap).replace(',', ' ')
    str_percs = '{:,.2f} '.format(percs).replace(',', ' ')
    str_cap = '{:,.2f} '.format(capital).replace(',', ' ')
    init_cap_sym = count_symbols(list(str_init.replace(' ', '1')))
    percs_sym = count_symbols(list(str_percs.replace(' ', '1')))
    capit_sym = count_symbols(list(str_cap.replace(' ', '1')))
    max_month = max(mon_lists)
    maxes = {'init_cap': init_cap_sym, 'percs': percs_sym, 'capital': capit_sym, 'months': max_month}
    return maxes

