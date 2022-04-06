import math


def czy_pierwsza(liczba):
    for x in range(2, int(liczba ** 0.5)+1):
        if liczba % x == 0:
            return False

    return True

def zad1():
    plik = open("czer_17/punkty.txt")

    ilosc = 0
    for linia in plik.readlines():
        wyniki = linia.split()
        pier1 = czy_pierwsza(int(wyniki[0]))
        pier2 = czy_pierwsza(int(wyniki[1]))

        if pier1 == True and pier2 == True:
            ilosc += 1

    print(ilosc)

    plik.close()


def pomoc2(liczba):
    lista = []
    for x in list(liczba):
        lista.append(int(x))

    return sorted(list(dict.fromkeys(lista)))

def zad2():
    plik = open("czer_17/punkty.txt")


    ilosc = 0
    for linia in plik.readlines():
        liczby = linia.split()

        l1 = pomoc2(liczby[0])
        l2 = pomoc2(liczby[1])

        if l1 == l2:
            ilosc += 1

    print(ilosc)

    plik.close()




def zad3():
    plik = open("czer_17/punkty.txt")
    linie = plik.readlines()

    punkty = {}
    odleglosc = 0
    for i in range(0, len(linie)-1):
        linia1 = linie[i][:-1].split()
        for j in range(i + 1, len(linie)-2):
            linia2 = linie[j][:-1].split()

            nowa_odl = round(math.sqrt(pow(int(linia1[0]) - int(linia2[0]),2) + pow(int(linia1[1]) - int(linia2[1]),2)))
            if nowa_odl > odleglosc:
                 odleglosc = nowa_odl
                 punkty = {"1": linia1, "2": linia2}

    print(odleglosc, punkty)


    plik.close()


def zad4():
    plik = open("czer_17/punkty.txt")

    a = 0
    b = 0
    c = 0

    for linia in plik.readlines():
        punkty =  linia.split()
        x = int(punkty[0])
        y = int(punkty[1])


        if x > -5000 and x < 5000 and y > -5000 and y < 5000:
            a +=1
        elif (x == -5000 or x == 5000) or (y == -5000 or y== 5000):
            b+=1
        else:
            c+=1

    print(a, b, c)
    plik.close()
