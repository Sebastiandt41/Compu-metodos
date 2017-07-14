#La matriz de covarianza

import numpy as np 
import matplotlib.pyplot 

datos = np.genfromtxt("room-temperature.txt",delimiter =',')

T1 = datos[1:,1]
T2 = datos[1:,2]
T3 = datos[1:,3]
T4 = datos[1:,4]

promT1 = np.mean(T1)
promT2 = np.mean(T2)
promT3 = np.mean(T3)
promT4 = np.mean(T4)

matrix = (T1,T2,T3,T4)

M = len(T1)
n = len(matrix)

print promT1,promT2,promT3,promT4,n 

Cov = [ ]

for i in range(n+1):
	for j in range(n+1):
		for k in range(M):
			Cov[i,j] = np.sum((datos[(k+1),(i+1)]-np.mean(datos[1:,(i+1)]))*(datos[(k+1),(j+1)]-np.mean(datos[1:,(j+1)])))/(M-1)
print Cov

			
		
			 
		
		


