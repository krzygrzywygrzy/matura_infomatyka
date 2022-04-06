def find_last(plik):
    items = []
    for line in plik.readlines():
        item = line.split(" ")[-1]
        items.append(item)

    return items


def zad1():
    plik1 = open("./18_czer/przyklad1.txt", "r")
    plik2 = open("./18_czer/przyklad2.txt", "r")

    ost1 = find_last(plik1)
    ost2 = find_last(plik2)

    ilosc = 0
    for i, item in enumerate(ost1):
        if item == ost2[i]:
            ilosc += 1

    plik1.close()
    plik2.close()

    zapis = open("18_czer/wynik4_1.txt", "w")
    zapis.write(str(ilosc))
    zapis.close()


def pom2(linia):
    splitted = linia.split()
    odd = 0
    even = 0
    for number in splitted:
        if (int(number) % 2) == 0:
            even += 1
        else:
            odd += 1

    if odd == 5 and even == 5:
        return True
    else:
        return False


def zad2():
    plik1 = open("./18_czer/przyklad1.txt", "r")
    plik2 = open("./18_czer/przyklad2.txt", "r")

    ilosc = 0
    for line1, line2 in zip(plik1, plik2):
        l1 = pom2(line1)
        l2 = pom2(line2)
        if l1 == True and l2 == True:
            ilosc += 1

    plik1.close()
    plik2.close()


def pom3(line):
    liczby = []
    splitted = line.split()
    for liczba in splitted:
        if liczba not in liczby:
            liczby.append(liczba)

    return liczby


def zad3():
    plik1 = open("./18_czer/przyklad1.txt", "r")
    plik2 = open("./18_czer/przyklad2.txt", "r")

    ilosc = 0
    linie = []
    for i, (line1, line2) in enumerate(zip(plik1, plik2)):
        ln1 = pom3(line1)
        ln2 = pom3(line2)

        if ln1 == ln2:
            ilosc += 1
            linie.append(i + 1)

    print(ilosc, linie)
    plik1.close()
    plik2.close()


def pomoc4(line):
    arr = []
    for x in line.split():
        arr.append(int(x))

    return arr


def zad4():
    plik1 = open("./18_czer/przyklad1.txt", "r")
    plik2 = open("./18_czer/przyklad2.txt", "r")
    zapis = open("./18_czer/wynik4_3.txt", "a")

    for line1, line2 in zip(plik1, plik2):
        arr = [*pomoc4(line1), *pomoc4(line2)]

        for x in sorted(arr):
            zapis.write(str(x) + " ")
        zapis.write("\n")

    plik1.close()
    plik2.close()
    zapis.close()
