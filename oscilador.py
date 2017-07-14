import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

#CONSTANTES
k = 42.0
g = 9.8 
miu = 0.15
t = np.linspace(0,3,5000)
m = 0.25
h = (3.0/4999.0)

#Definido por arrays 

x=np.zeros(5000)
x_prime= np.zeros(5000)
x_pprime= np.zeros(5000)

x[0]= 0.2 
x_prime[0]=0.0
x_pprime[0] = -((k/m)*x[0])+(g*miu)

for i in range(1,5000):
	x[i] = x_prime[i-1]*h +x[i-1]
	x_prime[i] = x_pprime[i-1]*h + x_prime[i-1]
	if x_prime[i] > 0:	
		x_pprime[i] = -(k/m)*x[i]-(g*miu)
	else:
		x_pprime[i] = -(k/m)*x[i]+(g*miu)

fig,var = plt.subplots(3,1)
var[0].plot(x,color = 'r')
var[0].set_ylabel('Posicion')
var[1].plot(x_prime,color="b")
var[1].set_ylabel('Velocidad')
var[2].plot(x_pprime,color="g")
var[2].set_ylabel('Aceleracion')
plt.suptitle("Oscilador")
plt.show()
plt.close()

#Definido por funciones ...
#Para el viernes transformada de Fourier de imagenes, plt.imread(), plt.imshow(),np.fft.fft2(),np.fft.ifft2().
 









