from numpy import count_nonzero as count_symbols


def print_block(obj, spaces, end=''):
    print('| {}'.format(obj), end='')
    print(' ' * (spaces - count_symbols(list(str(obj).replace(' ', '1')))), end=end)


def get_maxes(years, initial_capital, percent, investment_infusion):
    capital = initial_capital
    for year in range(years):
        for month in range(12):
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
    maxes = [init_cap_sym, percs_sym, capit_sym]
    return maxes

