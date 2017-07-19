import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation

datos = np.genfromtxt("datos.csv",delimiter=",")
n_cuerpos = 10

x=datos[:,0]
y=datos[:,1]
z=datos[:,2]

tfinal = len(x)/n_cuerpos
print tfinal
x1=np.zeros((10,tfinal))
y1=np.zeros((10,tfinal))
z1=np.zeros((10,tfinal))

for i in range(0,n_cuerpos):
	for t in range(0,tfinal):
		indice = int((10*t+i))
		x1[i,t] = x[indice]
		y1[i,t] = y[indice]
		z1[i,t] = z[indice]

fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')
sup = ax.plot(x1[0],y1[0],z1[0])
sup = ax.plot(x1[1],y1[1],z1[1])
sup = ax.plot(x1[2],y1[2],z1[2])
sup = ax.plot(x1[3],y1[3],z1[3])
sup = ax.plot(x1[4],y1[4],z1[4])
sup = ax.plot(x1[5],y1[5],z1[5])
sup = ax.plot(x1[6],y1[6],z1[6])
sup = ax.plot(x1[7],y1[7],z1[7])
sup = ax.plot(x1[8],y1[8],z1[8])
sup = ax.plot(x1[9],y1[9],z1[9])
#fig.colorbar(sup,shrink=0.5,aspect=5)
ax.set_xlabel(r"$UA$")
ax.set_ylabel(r"$UA$")
ax.set_zlabel(r"$UA$")
#plt.save("orbitas.png")
plt.show()
plt.close()

