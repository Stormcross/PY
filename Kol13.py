#Zadatak13 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf

def faktorijeli(n):
    c=0
    fak=1
    ost=0
    while c<(n-1):
        for i in range(1,n):
            a=i%n
            fak*=a
            c+=1
            ost = fak % n
    else:
        print("za broj ",n," koji ima faktorijel ",fak," i ostatak ",ost)

def ulaz(n):
    if n==int(n):
        faktorijeli(n)
    else:
        print("Unjeli ste krivi unos, pokušajte ponovo")
        ulaz()
n=input("Unesite broj n=")
ulaz(n)



#Radi wuhuu :D