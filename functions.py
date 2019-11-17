from numpy import count_nonzero as count_symbols


def print_block(obj, spaces, end=''):
    print('| {}'.format(obj), end='')
    print(' ' * (spaces - count_symbols(list(str(obj).replace(' ', '1')))), end=end)

