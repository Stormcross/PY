#Zadatak 3 http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf

n=int(input("Unesite cijeli broj n="))
n+=1
d=0

for a in range(1,n):

    if a==1 or a==2 or a==3:
        print(a)
    else:
        #provjera koliko ima djeljenika, ako ima samo 2 onda
        c=0
        for b in range(1,a):
           if a%b==0:
               c+=1
           else:
               pass
        if c<2:
            print(a)
        else:
            pass

#Works