#Zadatak 6 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf
n=int(input("Unesite broj <=10, n="))
if n<=10:
    for x in range(1,n+1):
        for y in range(1,x):
            if x%y==y-1:
                if y-1!=0:
                    print("x=",x,"y=",y,"y-1=",y-1)
else:
    print("Niste unjeli broj <=10!")

#Program radi ali ne kuzim kaj oceju u zadatku ?!