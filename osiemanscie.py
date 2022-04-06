def zad1():
    plik = open("./18/przyklad.txt")

    wynik = ""
    for i, odczyt in enumerate(plik.readlines()):
        if (i+1) % 40 == 0:
            wynik +=odczyt[9]

    plik.close()
    print(wynik)


def zad2():
   plik = open("./18/przyklad.txt")

   slowo = ""
   for linia in plik.readlines():
       x = list(dict.fromkeys(list(linia)[:-1]))
       if len(x) > len(slowo):
           slowo = linia[:-1]


   plik.close()
   print(slowo, len(slowo))



def pomoc3(linia):
    for x in range(0, len(linia)-1):
        if abs(ord(linia[x])-ord(linia[x+1])) > 10:
            return False

    return True

def zad3():
  plik = open("./18/przyklad.txt")

  for linia in plik.readlines():
      res  = pomoc3(linia[:-1])
      if res == True:
          print(linia[:-1])





  plik.close()