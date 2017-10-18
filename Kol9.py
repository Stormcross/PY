#Zadatak 9 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf

n=int(input("Unesite broj n, n="))
counter=0

for item in range(2,n):
    if n%(pow(item,2))==0:
        counter+=1

print("Ukupno=",counter)

#wuhuuu works