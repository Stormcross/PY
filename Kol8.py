#Zadatak 8 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf

from math import *

n=int(input("Unesite prirodni broj; n=")) #Gornja granica programa
#Trebamo m <= n koji u zadnjoj znamenki ima broj 9 u kvadratu
if n>=49:
    lista=[]
    for kv in range(1,n+1):
        if pow(kv,2)<=n:
            if pow(kv,2)%3==1:
                lista.append(pow(kv,2))

    lista1=[]
    for x in lista:
        if (x+1)%10==0:
            lista1.append(x)

    manji=lista1[0]
    veci=lista1[len(lista1)-1]
    print("\nnajmanji broj koji tražimo je ",manji)
    print("najveći broj koji tražimo je ",veci)

else:
    print("Nema!")

#wuhuu it works :)