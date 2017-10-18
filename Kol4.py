#Zadatak 4 http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf
from math import *
#Pitagora-> c=sqrt(sqr(a)+sqr(b))

hip=int(input("Unesite hipotenuzu: hip="))
phip=pow(hip,2)
a=0
b=0
lista=[]
for a in range(1,hip):
    b=sqrt(phip-pow(a,2))
    if b==int(b):
        lista.append(b)
        lista.sort()
c=0
for l in range(0,len(lista)-1):
    print("Stranica a=",lista[c],"\nStanica b=",lista[c+1],"\nHipotenuza c=",hip,"\n")
    c += 2

#Kvazi radi, daje kaj nam treba ali ima greške