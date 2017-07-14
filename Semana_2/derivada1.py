# forward differentiation
import numpy as np
import matplotlib.pyplot as plt 
def funcion (x):

	y = x*x 
	return y 

def derivadafd ():

	arreglo = np.linspace(0,10,1000)
	valor = funcion(arreglo)
	h = ((10.0-0.0)/(1000.0-1.0)) 
	
	valor2 = np.array(valor) 

	derivada = (((funcion(arreglo+h))-valor)/h)
	
	return derivada
	

print derivadafd()

def derivadacd():

	arreglo = np.linspace(0,10,1000)
	valor = funcion(arreglo)
	h = ((10.0-0.0)/(1000.0-1.0)) 
	
	valor2 = np.array(valor) 

	derivada = ((funcion(arreglo+(h*0.5))-funcion(arreglo-(h*0.5)))/h)
	
	return derivada
print derivadacd()

#Ahora corriendo el array

def derivadafdarray(a,b,n):

	arreglo = np.linspace(a,b,n)
	valor = funcion(arreglo)

	h = (b-a)/(n-1.0)
	w = arreglo[1] - arreglo[0]
	valort = funcion(arreglo+w/2)
	valorte = funcion(arreglo-w/2)
	derivadaarray = (valor[1:]-valor[:-1])/h
	#derivadaarray = (valort - valorte)/w
	
	return derivadaarray 
		
	
print derivadafdarray(0,10,100)


def derivadafdarray2h(a,b,n):

	arreglo = np.linspace(a,b,n)
	valor = funcion(arreglo)

	h = (b-a)/(n-1.0)
	w = arreglo[4] - arreglo[2]

	derivadaarray2 = (valor[2:]-valor[:-2])/(w)
	

	return derivadaarray2 
#EL numero de puntos es importante LOQUETE 		
print derivadafdarray2h(0,10,10000)


















