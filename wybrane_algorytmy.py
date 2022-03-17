def czy_pierwsza(liczba):
    for n in range(2, int(liczba ** 0.5) + 1):
        if liczba % n == 0:
            return False
        return True


def czy_doskonala(liczba):
    suma_dzielnikow = 1
    for x in range(2, liczba):
        if liczba % x == 0:
            suma_dzielnikow += x

    if suma_dzielnikow == liczba:
        return True
    else:
        return False


def na_czynniki_pierwsze(liczba):
    rozklad = []
    k = 2
    while liczba != 1:
        while liczba % k == 0:
            liczba //= k
            rozklad.append(k)

        k += 1
    return rozklad


def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a


def nww(a, b): return a * b // nwd(a, b)
