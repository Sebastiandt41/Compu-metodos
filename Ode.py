import numpy as np 
import matplotlib.pyplot as plt 

#ODE's 

#Euler method 
b = 1
a = 0
n = 1000
puntos = np.linspace(a,b,n)
h = float((b-a)/(n-1.0))	

x = np.zeros(n)
y = np.zeros(n)


def funcion_p(x,y):
	
	return 1+y*y


#for i in range(0,n-1):
#	x[i+1] = x[i] + h 
#	y[i+1] = y[i] + h*funcion_p(x[i],y[i])
	

#Leap-frog - center difference
#x[1] = a+h
#y[1] = y[0] + h*funcion_p(x[0],y[0])
#for i in range(1,n-1):
#	x[i+1] = x[i] + h 
#	y[i+1] = y[i-1] + 2*h*funcion_p(x[i],y[i])
	

x[0] = a
y[0] = 0

#Runge-kutta 4 order 

for i in range(0,n-1):
	
	k1 = k1 = h*funcion_p(x[i],y[i])
	k2 = h*funcion_p(x[i]+(0.5*h),y[i]+(0.5*k1))
	k3 = h*funcion_p(x[i]+(0.5*h),y[i]+(0.5*k2))
	k4 = h*funcion_p(x[i]+h,y[i]+k3)

	prom = ((k1+(2.0*k2)+(2.0*k3)+k4))*(0.166666666)

	x[i+1] = x[i] + h
	y[i+1] = y[i] + prom
	

plt.scatter(x,y)
plt.show()
plt.close()




















