a=[1,4]
b=[2,5,2,2]
a2=[5,9,9,9,9]
b2=[4,9]
def test_lista(a,b2):
	c1=-1
	for x in a:
		c1 += 1
		c2=-1
		for y in b2:
			c2 += 1
			if x==y:
				print("prijateljski: ",a[c1],b2[c2])
				break

test_lista(a,b2)