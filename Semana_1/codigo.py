
n = input("Introduzca unnumero para hacer la conjetura")

lista =[]

while n > 1:
	if n%2==0:
		lista.append(n/2)
		n = n/2
	else:
		lista.append((3*n)+1)
		n = (3*n) +1 

print lista 
