import numpy as np 
import matplotlib.pyplot as plt 

#Definir los distintos metodos de resolucion de PDES : 1. Conveccion lineal 2. Conveccion no lineal 3. Difusion 4. Conveccion + Difusion. Ademas ; delta t = alpha(<1 , 0.5 )*(delta x)**2

#1.Conveccion lineal 

n = 80
pasos = 300
x = np.linspace(0.0,2.0,n)
alpha = 0.5
dx = x[1]-x[0]
dt = 0.001
#dx = (np.sqrt((dt/alpha)))
#dt = alpha*(dx)**2
dif = 0.3
c = 1.0
u = np.ones(n) 

u[np.where((x<1.25)&(x> 0.75))] = 2

def Conv_lineal():
	for v in range(pasos):	
	#Copy se asegura de guardar la informacion actual 
		u_anterior = u.copy() 	
		for i in range(1,n-1): 
        		u[i] = u_anterior[i] - c*dt/dx*(u_anterior[i]-u_anterior[i-1])
	return u
 
#2. Conveccion no lineal 

def Conv_nolineal():
	for v in range(pasos):		
		u_anterior = u.copy() 	
		for i in range(1,n-1): 
        		u[i] = u_anterior[i] - u_anterior[i]*dt/dx*(u_anterior[i]-u_anterior[i-1])

	return u

#3. Difusion , CORREGIR 
def Difusion():
	for v in range(pasos):		
		u_anterior = u.copy() 	
		for i in range(1,n-1): 
        		u[i] = dif*alpha*u_anterior[i+1] + (1-(2*dif*alpha))*- u_anterior[i]+ dif*alpha*u_anterior[i-1]
	return u 

plt.plot(x,Difusion())
plt.show()
plt.close()



