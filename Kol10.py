#Zadatak 10 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf

def s(i):
    djeljenici=[]
    for x in range(1,i):
        if i%x==0:
            djeljenici.append(x)
    suma=sum(djeljenici)
    return suma



def pregled(i,n):
    if i<n:
        print("Ovaj broj je manjkav jer je ",i,"<",n)
    elif i==n:
        print("Ovaj broj je savršen jer je ",i,"=",n)
    else:
        print("Ovaj broj je oblian jer je ",i,">",n)

#_____________________________________________________

n=int(input("Unesite prirodan broj n="))
i=s(n)
pregled(i,n)

#Workssss


