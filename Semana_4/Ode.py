import numpy as np 
import matplotlib.pyplot as plt 

#ODE's 

#Euler method 
b = 1
a = 0
h = 0.1
n = int(((b-a)/h)+1.0)
puntos = np.linspace(a,b,n)
#h = float((b-a)/(n-1.0))	

x = np.zeros(n)
y = np.zeros(n)

x[0] = a
y[0] = 0

def funcion_p(x,y):
	
	return 1+y*y

def euler():
	for i in range(0,n-1):
		x[i+1] = x[i] + h 
		y[i+1] = y[i] + h*funcion_p(x[i],y[i])
	return x,y

#Leap-frog - center difference
def leap():
	x[1] = a+h
	y[1] = y[0] + h*funcion_p(x[0],y[0])
	for i in range(1,n-1):
		x[i+1] = x[i] + h 
		y[i+1] = y[i-1] + 2*h*funcion_p(x[i],y[i])
	
	return x,y

#Runge-kutta 4 order 
def runge():
	for i in range(0,n-1):
	
		k1 = k1 = h*funcion_p(x[i],y[i])
		k2 = h*funcion_p(x[i]+(0.5*h),y[i]+(0.5*k1))
		k3 = h*funcion_p(x[i]+(0.5*h),y[i]+(0.5*k2))
		k4 = h*funcion_p(x[i]+h,y[i]+k3)

		prom = ((k1+(2.0*k2)+(2.0*k3)+k4))*(0.166666666)

		x[i+1] = x[i] + h
		y[i+1] = y[i] + prom
	return x,y
	

plt.plot(euler()[0],euler()[1],color='g',label ='Euler m.')
plt.plot(leap()[0],leap()[1],color='b',label='Leap-frog m.')
plt.plot(runge()[0],runge()[1],color='r',label='Runge-Kutta.')
plt.title("Ordinary differencial equations methods")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc =0)
plt.show()
plt.close()




















