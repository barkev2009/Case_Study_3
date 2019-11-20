from functions import *
from matplotlib.pyplot import *

langchoice = input('Пожалуйста, выберите язык. Please, choose the language. ')
if langchoice.lower() == 'english' or langchoice.lower() == 'английский':
    from ENG import *
elif langchoice.lower() == 'russian' or langchoice.lower() == 'русский':
    from RUS import *

years = int(while_print(period_lit, failure))
initial_capital = float(while_print(init_cap_lit, failure))
percent = float(while_print(per_lit, failure))
investment_infusion = float(while_print(inv_fuse, failure))

if langchoice.lower() == 'english' or langchoice.lower() == 'английский':
    maxes = get_maxes(years, initial_capital, percent, investment_infusion, 'eng')
elif langchoice.lower() == 'russian' or langchoice.lower() == 'русский':
    maxes = get_maxes(years, initial_capital, percent, investment_infusion, 'rus')


# Setting design elements
month_block_width = max(maxes['months'], count_symbols(mon_block_lit))
init_block_width = max(maxes['init_cap'], count_symbols(init_block_lit), count_symbols(base))
per_block_width = max(maxes['percs'], count_symbols(per_block_lit), count_symbols(dur_month))
cap_block_width = max(maxes['capital'], count_symbols(cap_block_lit))
dashes = '-' * (9 + month_block_width + init_block_width + per_block_width + cap_block_width)

capital = initial_capital
x_vector = []
y_vector = []
for year in range(years):

    # Header
    print(year_lit.format(year + 1))

    print(dashes)
    print_block(' ', month_block_width)
    print_block(base, init_block_width)
    print_block(per_block_lit, per_block_width)
    print_block(' ', cap_block_width, end='|\n')

    print_block(mon_block_lit, month_block_width)
    print_block(init_block_lit, init_block_width)
    print_block(dur_month, per_block_width)
    print_block(cap_block_lit, cap_block_width, end='|\n')

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
ax.set_xlabel(time_lit)
ax.set_ylabel(cap_lit)
ax.set_title(cap_growth, fontsize=15)
show()
