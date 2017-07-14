import numpy as np 
import matplotlib.pyplot as plt

#Funcion dada
def funcion(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
	y = (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)**3
	return y

#Retorna el resultado de la integral para la funcion dada utilizando del metodo de Monte-Carlo de mean value
def inmontecarlo(N):

	max_x = 2
	min_x = 0

	x1= (max_x-min_x)*(np.random.rand(N))+ min_x
	x2= (max_x-min_x)*(np.random.rand(N))+ min_x
	x3= (max_x-min_x)*(np.random.rand(N))+ min_x
	x4= (max_x-min_x)*(np.random.rand(N))+ min_x
	x5= (max_x-min_x)*(np.random.rand(N))+ min_x
	x6= (max_x-min_x)*(np.random.rand(N))+ min_x
	x7= (max_x-min_x)*(np.random.rand(N))+ min_x
	x8= (max_x-min_x)*(np.random.rand(N))+ min_x
	x9= (max_x-min_x)*(np.random.rand(N))+ min_x
	x10=(max_x-min_x)*(np.random.rand(N))+ min_x
	
	y = funcion(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10)
	
	resultado = np.mean(y)*(max_x-min_x)**10
	return resultado 

#Repite el metodo anterior 20 veces y toma como resultado de la integral el promedio de las 20 repeticiones
def integral(N):
	result = 0
	i = 0
	while i < 20:
		result += inmontecarlo(N)
		i+= 1
		 
	integral = result/20.0

	return integral

integral_analitica = 1126400.0

#Retorna el valor de la integral para distinos valores de N , ademas del error de estos valores de la integral 
def variandoN():
	n = 2
	N = []
	Valor = []
	i = 0
	error = []
	
	while i < 13:
		integralN = integral(n)
		errore =  abs((integral_analitica - integralN)/integral_analitica)
		i+= 1
		n = 2**i
		N.append(n)
		error.append(errore)
		Valor.append(integralN)
		
	return Valor , N , error

y,x,error = variandoN()
uno_sobre = 1/(np.sqrt(x))
plt.scatter(uno_sobre, error)
plt.title("Error")
plt.xlabel("1/sqrt(N)")
plt.ylabel("Error")
plt.savefig("err_integral.pdf",format='pdf')
plt.close()
plt.plot(x,y)
plt.title("Integral")
plt.xlabel("N")
plt.ylabel("Valor integral")
plt.savefig("num_integral.pdf",format='pdf')
plt.close()



















	

	
	
