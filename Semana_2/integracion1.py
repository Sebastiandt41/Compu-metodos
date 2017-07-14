import numpy as np 
import scipy as sci 
import math 

def sen (angulo):
	y = np.sin(angulo*(np.pi/180.0))
	return y 

#la otra manera es con linspace de sen del intervalo luego le hago la suma y luego lo otro. 

def integracion (a , b):
	
	yinteger =[]
	w = ((b-a)/(90-1.0))
	for i in range (a,b):
		
		if i == a or i == b:
			
			yinteger.append((sen(i)/2.0)*w)
		
		else:
		
			yinteger.append((2*sen(i)/2.0)*w)

	
	integral = (np.sum(yinteger))
	
	return integral 


print integracion (0 , 90 )



def funcionseno (a,b,n):

	array = np.linspace (a , b , n)
	y = np.sin(array)
	
	return y

def integraciondos (a,b,n):

	valor = funcionseno(a, b, n)
	w = ((b-a)/(n-1))
	suma = ((valor[0]/2.0) + np.sum(valor[1:-1]) + (valor[-1]/2.0))
	integral = suma*w
	return integral 

print integraciondos(0,np.pi*0.5,1000000)

	
			
		
	


