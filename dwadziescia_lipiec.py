def z1():
    maks = 0
    lista = []

    plik = open("20/identyfikator_przyklad.txt", "r")
    for linia in plik.readlines():
        cyfry = list(linia)[3:-1]
        suma = 0
        for cyfra in cyfry:
            suma += int(cyfra)

        if suma > maks:
            maks = suma
            lista = [linia]
        elif suma == maks:
            lista.append(linia)

    plik.close()
    plik = open("20/wyniki4_1.txt", "a")
    for x in lista:
        plik.write(x)

    plik.close()


def z2():
    file = open("20/identyfikator_przyklad.txt", "r")
    write = open("20/wyniki4_2.txt", "a")

    for linia in file.readlines():
        seria = list(linia[0:3])
        liczba = list(linia[3:-1])

        if seria == seria[::-1] or liczba == liczba[::-1]:
            write.write(linia)

    file.close()
    write.close()


def mnoznik(liczba):
    reszta = liczba % 3
    match reszta:
        case 0:
            return 7
        case 1:
            return 3
        case 2:
            return 1
        case _:
            return 0

def z3():
    plik = open("20/identyfikator_przyklad.txt")
    zapis = open("20/wyniki4_3.txt", "a")

    for linia in plik.readlines():
        seria = list(linia[0:3])
        pierwsza = int(linia[3])
        liczby = list(linia[4:-1])

        suma_seria = 0
        for i, litera in enumerate(seria):
            wartosc = int(ord(litera)) - 55
            suma_seria += mnoznik(i) * wartosc

        suma_liczby = 0
        for i, liczba in enumerate(liczby):
             suma_liczby += mnoznik(i)* int(liczba)

        if (suma_liczby + suma_seria) % 10 != pierwsza:
            zapis.write(linia)

    zapis.close()
    plik.close()

