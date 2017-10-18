#Zadatak 1 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf

k=0
k= int(input("Unesite cijeli broj: "))
suma=0
djeljenik=1

while djeljenik<=k:
    if k%djeljenik==0:
        print(djeljenik)
        suma+=djeljenik
        djeljenik+=1
    else:
        djeljenik+=1

if k<suma:
    print("Ovo je obilan broj jer je ",k,"<",suma)
else:
    print("Ovo nije obilan broj jer je ", k, ">", suma)

#Works