#Zadatak 11 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf

def akoobilan(i):
    djeljitelji=[]
    for x in range(1,i):
        if i%x==0:
            djeljitelji.append(x)
    suma=sum(djeljitelji)
    return suma


def provjera(k,m):
    obilni=[]
    c=0
    for i in range(k,m):
        if akoobilan(i)>i:
            obilni.append(i)
            c+=1
    print("najmanji obilni broj je ",obilni[0],"\nA ukupno ih ima ",c, "komada")

k=int(input("Unesite K="))
m=int(input("Unesite M="))
provjera(k,m)

#Ma ja sam car <3

