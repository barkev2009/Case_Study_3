def isfloat(var):
    try:
        var = float(var)
        return True
    except ValueError:
        return False

a = '9.5'

print(isfloat(a))