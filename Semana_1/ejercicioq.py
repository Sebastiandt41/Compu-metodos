
import numpy as np 
import matplotlib.pyplot as plt

sismos = np.loadtxt("signif.txt",dtype = str,delimiter ='\t')

x = sismos[: , 20]
y = sismos[: , 21]

#print (x,y)


x_plot =[]
y_plot =[]

#Esta funcion prueba si el valor de la lista es un float o no , tomado de : https:\\stackoverflow.com\questions\379906\parse-string-to-float-or-int

def isfloat(value):
	try:
		float(value)
		return True
	except:
		return False 
 

for i in range (len(x)) :
	
	a = x[i]
	b = y[i]

	if isfloat(a) == False or isfloat(b) == False:
		continue
		
	else:
		x_plot.append(x[i])
		y_plot.append(y[i])


plt.scatter(y_plot, x_plot , c ="red" , alpha = 0.9)
plt.xlabel ("Longitud")
plt.ylabel ("Latitud")
plt.title("Quakes")
plt.savefig("quakes" , format = "png")
plt.show()

#Elaborado por Juan Sebastian Duran Torres.
