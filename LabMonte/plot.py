import numpy as np 
import matplotlib.pyplot as plt

datos = np.genfromtxt("datos.csv")

y = datos[:,0]
yp = datos[:,1]
x = datos[:,2]

plt.plot(x,y,label="real")
plt.plot(x,yp,label="estocastico")
plt.legend()
plt.show()
plt.close()

