
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, norm


datos = np.loadtxt('datos_CAMINATA.txt') 

#1. Histograma 

binomial = datos[0]
plt.hist(binomial ,  normed = True)
plt.title("Binomial")
plt.savefig("Binomial" , format = "png" , bins = 50)
plt.close()

#2. Lista de sumas 

x = len(datos)

datos2 = []

for i in range (x):
	valor = np.sum(datos[i])
	datos2.append(valor)

#3. Segundo histograma 

plt.hist(datos2 , normed = True)


#4.Fit de la nueva distribucion

a,b = norm.fit(datos2)
x = np.linspace(3200,3800,1000)
y = norm.pdf(x,a,b)
plt.plot(x,y)
plt.title("Normal")
plt.savefig("Normal",format = "png", bins =50)

# La media de la distribucion normal es de "a" 

#5. Sabiendo que la distribucion binomial esta dada por: u(normal) = n*u(binomial) ...
#Ademas sabiendo que u(binomial) = N*p
n = 1000.0
N = 10.0
ubinomial = a/n
prob = ubinomial/N

print "La probabilidad de sacar una cara con esta moneda es :" , prob








