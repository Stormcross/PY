# Zadatak 14 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf
from math import pow, sqrt
def kvadrat(a):
    korijen = sqrt(a)
    korijen = int(round(korijen, 0)) #Zaokružimo broj da okvirno dobijemo gornju granicu
    lista_rez = []
    granicnik_ostatka=int(input("Unesite max dozvoljeni ostatak o="))
    for i in range(2, korijen + 1):
        k = 2
        while k < korijen:
            kvad = int(pow(i, k))
            k += 1
            b = a % kvad
            if 0 <= b <= granicnik_ostatka: #Računamo s razlikom od vrijednosti ostatka 2
                lista_rez.append(i)

            konacno = set(lista_rez)
    print("Broj za koji tražimo najbliži kvadrat n=",a,"\nBrojevi čija potencija s ostatkom ",granicnik_ostatka,"\nsu najbliže našem broju->", konacno)


def ulaz(n):
    if n >= 4:
        kvadrat(n)
    else:
        print("Unjeli ste krivi broj, pokušajte ponovo")
        a = int(input("Unesite broj"))
        ulaz(a)


n = int(input("Unesite broj n="))
ulaz(n)

#Radi! ..Nema zajebancije samo snažno