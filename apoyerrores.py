#Self se refiere a los parametros propios de la clase.

#La tarea , campo electrico es menos el gradiente del potencial , pregunta como creo muchos objetos con un for, con parametros diferentes. 

#ERRORES

import numpy as np
import matplotlib.pyplot as plt 
def funcion (x):

	y = np.cos(x)
	return y 

def funccomparar(x):
	yr = -np.sin(x)
	return yr

def derivadas(a,b,h):

	n = ((b-a)/h) +1
	arreglo = np.linspace(a,b,n)

	valor = funcion(arreglo)
	valor2 = funccomparar(arreglo)	
	
	#valor2 = np.array(valor) 
	#FW
	derivadafd = (((funcion(arreglo+h))-valor)/h)
	#BD 
	derivadabd = (((valor)-funcion(arreglo-h))/h)
	#CD
	derivadacd = ((funcion(arreglo+(h*0.5))-funcion(arreglo-(h*0.5)))/h)
	#ED
	derivadaed = ((4.0*(funcion(arreglo+(h*0.25))-funcion(arreglo-(h*0.25)))/h*0.5-derivadacd)/3.0)
	
	return derivadafd,derivadabd,derivadacd,derivadaed,valor2,h

erroresfw = []
erroresbd = []
errorescd = []
erroresed = [] 
hreal = []
i = 0.000001
while i < 0.1:

	
	derivadafd,derivadabd,derivadacd,derivadaed,valor2,h = derivadas(0,np.pi*0.5,i)
	erroresfw.append(abs(derivadafd[15] - valor2[15]))
	erroresbd.append(abs(derivadabd[15] - valor2[15]))
	errorescd.append(abs(derivadacd[15] - valor2[15]))
	erroresed.append(abs(derivadaed[15] - valor2[15]))
	hreal.append(i)
	i = i*10
	
plt.loglog(hreal,erroresfw,label = "FW")
plt.loglog(hreal,erroresbd ,label = "BD")
plt.loglog(hreal,errorescd,label = "CD")
plt.loglog(hreal,erroresed,label = "ED")

plt.xlabel ("h")
plt.ylabel ("Error")
plt.title("Error vs H en derivadas")
plt.savefig("Error_vs_h" , format = "png")
plt.legend()
plt.show()














	
