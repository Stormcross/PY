#Zadatak 15 - http://degiorgi.math.hr/prog1/materijali/p1-zadaci_za_prakticni_kolokvij.pdf
def djeljitjelj(n):
	lista=[]
	for x in range(1,n):
		if n%x==0:
			lista.append(x)
			for y in lista:
				y=int(y)
	lista_sum_1=sum(lista)
	return(lista_sum_1)	#Imamo sumu djeljitelja broja

print("Suma svih djeljitelja od broja 220 =",djeljitjelj(220))
print("Suma svih djeljitelja od broja 284 =",djeljitjelj(284))
print("Suma svih djeljitelja od broja 496 =",djeljitjelj(496))

def main(n):
	if n>283:
		lista_svih_suma_1=[] #ovdje cemo spremiti sve sume
		obradeni_brojevi_1=[] #Brojevi za koje smo dobili djdelitelje
		lista_svih_suma_2=[]
		obradeni_brojevi_2=[]
		
		counter=-1 #counter da dobijemo poziciju na listi
		
		for k in range(220,n+1):	# Dobijemo sumu djelitelja za naš broj
			lista_svih_suma_1.append(djeljitjelj(k))
			obradeni_brojevi_1.append(k)
		for l in range(283,n+1):
			lista_svih_suma_2.append(djeljitjelj(l))
			obradeni_brojevi_2.append(l)
		
		print("\n","obradeni_brojevi_1:",obradeni_brojevi_1,"\n")
		print("\n","lista_svih_suma_1",lista_svih_suma_1,"\n")
		print("\n","obradeni_brojevi_2",obradeni_brojevi_2,"\n")		
		print("\n","lista_svih_suma_2",lista_svih_suma_2,"\n")

		test_lista(obradeni_brojevi_2,obradeni_brojevi_1,lista_svih_suma_1,lista_svih_suma_2)

	else:
		print("Najmanji prijateljski broj je kombinacija 220 i 284,\nUnesite veći broj od 283: ")
		broj=int(input("Unesite ponovo broj broj: "))
		main(broj)

def test_lista(a,b,c,d):
	c1=-1
	for x in a: #pretrazivanje prve liste obrađeni brojevi 2 -> 284 
		c1 += 1
		c2=-1
		for y in c: #Pogleda ako u listvi suma 1 ima broj 284 (suma od 220)
			c2 += 1
			if x==y and b[c2]==d[c1]:
				if a[c1]==d[c1]:
					print("Savršeni broj",d[c1]," nije prijateljski.\n")
				else:
					print("a = obradeni_brojevi_2")
					print("b = obradeni_brojevi_1")
					print("c = lista_svih_suma_1")
					print("d = lista_svih_suma_2\n")
					print("prijateljski: a=",a[c1],"b=",b[c2],"\n")
					break

broj=int(input("Unesite broj: "))
main(broj)

#Works :)