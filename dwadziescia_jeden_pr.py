def z1():
    file = open("21_pr/galerie_przyklad.txt", "r")

    malls = {}
    for line in file.readlines():
        splitted = line.split()[0]
        if splitted in malls:
            malls[splitted] = malls[splitted] + 1
        else:
            malls[splitted] = 1

    file.close()

    file = open("21_pr/wynik4_1.txt", "a")
    for key in malls:
        file.write(key + " " + str(malls[key]) + "\n")


def z2():
    file = open("21_pr/galerie_przyklad.txt")

    minn = 9999999
    maxx = -1
    minCityName = ""
    maxCityName = ""

    malls = {}
    for line in file.readlines():
        city = line.split()[1]
        splitted = line.split()[2:]

        total_shops = 0
        total_area = 0
        for x in range(0, len(splitted), 2):
            if int(splitted[x]) != 0:
                total_shops += 1
                total_area = total_area + int(splitted[x]) * int(splitted[x + 1])
        if total_area > maxx:
            maxx = total_area
            maxCityName = city
        if total_area < minn:
            minn = total_area
            minCityName = city


        malls[city] = [str(total_area), str(total_shops)]

    file.close()
    file = open("21_pr/wynik4_2a.txt", "a")
    for key in malls:
        file.write(key + " " + malls[key][0] + " " + malls[key][1] + "\n")
    file.close()

    file = open("21_pr/wynik4_2b.txt", "a")
    file.write(maxCityName + " " + str(maxx) + "\n")
    file.write(minCityName + " " + str(minn))



def z3():
    file = open("21_pr/galerie_przyklad.txt", "r")

    max_miasto = ""
    max_liczba = 0
    min_miasto = ""
    min_liczba = 100

    for line in file.readlines():
        miasto = line.split()[1]
        splitted = line.split()[2:]
        shops = []
        for x in range(0, len(splitted), 2):
            if int(splitted[x]) != 0:
                shops.append(int(splitted[x]) * int(splitted[x+1]))

        amount = len(list(dict.fromkeys(shops)))
        if amount > max_liczba:
            max_liczba = amount
            max_miasto = miasto
        if amount < min_liczba:
            min_liczba = amount
            min_miasto = miasto

    file.close()
    file = open("21_pr/wynik4_3.txt", "a")
    file.write(max_miasto + " " + str(max_liczba) + "\n")
    file.write(min_miasto + " " + str(min_liczba) + "\n")