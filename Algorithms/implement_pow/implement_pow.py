def power(x, y):
    if (y == 0): return 1
    temp = power(x, int(y / 2))

    if (y % 2 == 0):
        return temp * temp
    else:
        if (y > 0):
            return x * temp * temp
        else:
            return (temp * temp) / x

x, y = 2, 10
print('%.1f' % (power(x, y)))
