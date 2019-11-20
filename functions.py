from numpy import count_nonzero


def count_symbols(obj):
    answer = count_nonzero(list(obj.replace(' ', '1')))
    return answer


def print_block(obj, spaces, end=''):
    print('| {}'.format(obj), end='')
    print(' ' * (spaces - count_symbols(obj)), end=end)


def get_maxes(years, initial_capital, percent, investment_infusion, lang):
    global init_cap, percs
    if lang == 'eng':
        from ENG import months
    elif lang == 'rus':
        from RUS import months

    mon_lists = []
    for month in months:
        mon_lists.append(2 + count_symbols(month))

    capital = initial_capital
    for year in range(years):
        for month in months:
            init_cap = capital
            percs = capital * percent / 100
            capital += percs
            capital += investment_infusion
    str_init = '{:,.2f} '.format(init_cap).replace(',', ' ')
    str_percs = '{:,.2f} '.format(percs).replace(',', ' ')
    str_cap = '{:,.2f} '.format(capital).replace(',', ' ')
    init_cap_sym = count_symbols(str_init)
    percs_sym = count_symbols(str_percs)
    capit_sym = count_symbols(str_cap)
    max_month = max(mon_lists)
    maxes = {'init_cap': init_cap_sym, 'percs': percs_sym, 'capital': capit_sym, 'months': max_month}
    return maxes


def isfloat(var):
    try:
        float(var)
        return True
    except ValueError:
        return False


def while_print(name=None, answer=None):
    var = ''
    while var == '':
        var = input(name)
        if isfloat(var):
            return var
        elif var == '' or var.isdigit() == False:
            var = ''
            print(answer)
    return var
