import numpy as np 
import matplotlib.pyplot as plt

datos = np.genfromtxt("datos.csv")

y = datos[:,0]
yp = datos[:,1]
x = datos[:,2]

plt.plot(x,y)
plt.plot(x,yp)
plt.show()
plt.close()

