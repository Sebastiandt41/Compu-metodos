
#Implementacion propia de Fourier 

import numpy as np
import matplotlib.pyplot as plt 
import scipy as sci
from scipy import fftpack 


n = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1.0 / (f * 32.0 ) #32 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)

y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t)

#plt.plot(t,y)
#plt.plot(t,y, 'ko')
plt.xlabel('time(s)')
plt.ylabel('y(t)')

listareal = []

#def fourier():
	#i = 0
	#a1=[]
	#b1=[]
	#for i in t:
		#a = 0
		#b = 0
		#for valor in y:				
			#a += valor*np.cos(2*(np.pi)*f*dt*t[i])
			#b += valor*np.sin(2*(np.pi)*f*dt*t[i])
			#i+= 1
			#a1.append(a)
			#b1.append(b)		
	#return listareal
#lostfrequencies = int(dt)
#plot = fourier()
#plotreal = plot*lostfrequencies	

#plt.plot(fourier())
#plt.show()
#plt.close()



#EJERCICIO 

magnitud = np.genfromtxt("magnitude.dat",delimiter =" ") 
fase = np.genfromtxt("phase.dat",delimiter = " ")

Componentex = magnitud*np.cos(fase)
Componentey = magnitud*np.sin(fase)


parainvertir = Componentex + (Componentey*1j)


#magnitud =sqrt(x^2+y^2)
#fase = arctan (y/x)

print parainvertir

Inversa = sci.fftpack.ifft2(parainvertir)
inversa = abs(Inversa)
#o numpy.real

plt.imshow(inversa)
plt.savefig("secret.jpg")
plt.show()
plt.close()





















