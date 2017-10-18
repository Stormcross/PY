#Zadatak 5 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf
broj=int(input("Unesite broj: n="))
if broj>=6:
    lista = []
    for x in range(2,broj+1):
        del lista[:]
        for y in range(1,x):
            if x%y==0:
                lista.append(y)
                sum_lista=sum(lista)
                if sum_lista==x:
                    print("Ovo je savršeni broj: ",x)


else:
    print("Nema savršenog broja između 0 i ",broj)

#Wuhuu radi sve kak spada :)