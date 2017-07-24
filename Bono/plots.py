import numpy as np 
import matplotlib.pyplot as plt 

datos = np.genfromtxt("datos.csv")

x = datos[:,0]
y = datos[:,1]

plt.plot(x,y)
plt.ylim((0,2.2))
plt.show()
plt.close()
