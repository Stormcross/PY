#Zadatak12 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf
from math import pow
from sys import exit

def provjera(n):
    limit=100 #programski limit koji definira se ovdje u skripti
    brojac = 0
    lista_rez=[] #Lista rezultata
    for a in range(0,limit):
        for b in range(0,limit):
            c=pow(a,2)+pow(b,2)
            c=int(c)
            lista_rez.append(c)
            lista_rez.sort()
        for i in lista_rez:
            brojac=lista_rez.count(i)
            if brojac==n:
                kraj(i)
        else:
            brojac=0


def kraj(i):
    print("Najmanji rezultat suma dvaju kvadrata koji se pojavljuje ",n," puta je ",i)
    exit()

n=int(input("unesi n="))
provjera(n)

#Riješeno s limitom u programu, može biti postavljen prema potrebi ali u ovu svrhu je 100, max number je (100^2x100^2)