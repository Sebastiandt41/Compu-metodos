import numpy as np 
import matplotlib.pyplot as plt 

datos = np.genfromtxt("datos.csv")

x = datos[:,0]
y = datos[:,1]
y0 = datos[:,2]

plt.plot(x,y)
plt.plot(x,y0)
plt.ylim((-0.2,2.2))
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Conveccion lineal")
plt.savefig("conveccion.png")
#plt.show()
plt.close()
