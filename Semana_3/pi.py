#Calcular el valor de PI 

import numpy as np 
import matplotlib.pyplot as plt 

def funcion(x):
	y = 4/(1+(x*x))
	return y
#PI SE DEFINE COMO LA INTEGRAL DE 0 A 1 

def funcionpi(n):
	array = np.linspace(0,1,n)
	ye = funcion(array)
	return ye 

def integral(n):
	pi = 0
	circulo = funcionpi(n)
	w = 1.0/(n-1.0)
	for i in circulo:
		pi+= i*w
		 
	return pi 

print integral(100000000.0)
