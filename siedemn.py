def zad1():
    plik = open("17/dane.txt")

    jas = 0
    ciemn = 300

    for line in plik.readlines():
        for pixel in line.split():
            if int(pixel) > jas:
                jas = int(pixel)
            elif int(pixel) < ciemn:
                ciemn = int(pixel)

    print(jas, ciemn)

    plik.close()


def zad2():
    plik = open("17/dane.txt")

    ilosc = 0

    for linia in plik.readlines():
        lista = linia.split()[:-1]

        if lista != lista[::-1]:
            ilosc += 1

    print(ilosc)
    plik.close()


def zad3():
    plik = open("17/dane.txt")
    arr = []

    for line in plik.readlines():
        splitted = line.split()
        arr.append([int(x) for x in splitted])

    ilosc = 0
    for x, sub in enumerate(arr):
        for y in sub:
            if x < len(arr)-1 and abs(arr[x][y] - arr[x+1][y]) > 128:
                ilosc += 1
                break

            if x > 0 and abs(arr[x-1][y] - arr[x][y]) > 128:
                ilosc +=1
                break

            if y < len(sub)-1 and abs(arr[x][y] - arr[x][y+1]):
                ilosc +=1
                break

            if y > 0 and abs(arr[x][y-1] - arr[x][y]):
                ilosc += 1
                break

    print(ilosc)

    plik.close()
