import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


puntos = 30
a = 0.0
b = 30.0
c = 1.0
x = np.linspace(a,b,puntos)
y = np.linspace(a,b,puntos)
tfinal = 60

nu = 0.3
sigma = 0.
dx = b-a/puntos-1.0
dy = b-a/puntos-1.0
dt = sigma*dx**2/nu
alpha = c*dt/dx**2
z = np.zeros((puntos,puntos))
X,Y = np.meshgrid(x,y)

z[1:-1,1:-1]=2

#print z[:,0],z[0,:],z[:,-1],z[-1,:]

posx = int(0.5*len(x))
posy = int(0.33*len(y))

z[posx,posy]=-0.5    #Perturbacion

#fig = plt.figure()
#ax = fig.gca(projection ='3d')
#sup = ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap ='copper')
#plt.show()
#plt.close()

z1 = np.zeros((puntos,puntos))
for i in range(1,puntos-1):
	for j in range(1, puntos-1):
		z1[i,j] = z[i,j]+((alpha**2)/2.0)*z[i+1,j+1]-2*z[i,j]+z[i-1,j-1]

	
fig = plt.figure()
ax = fig.gca(projection ='3d')
sup = ax.plot_surface(X,Y,z1,rstride=1,cstride=1,cmap ='copper')
plt.show()
plt.close()














