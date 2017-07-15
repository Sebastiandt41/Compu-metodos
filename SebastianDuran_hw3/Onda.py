import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


puntos = 50
a = 0.0
b = 30.0
c = 1.0
x = np.linspace(a,b,puntos)
y = np.linspace(a,b,puntos)
tfinal = 30

nu = 0.3
sigma = 0.2
dx = b-a/puntos-1.0
dy = b-a/puntos-1.0
dt = sigma*dx**2/nu
alpha = c*dt/dx**2
z = np.zeros((puntos,puntos))
X,Y = np.meshgrid(x,y)

#z[1:-1,1:-1]=2

#print z[:,0],z[0,:],z[:,-1],z[-1,:]

posx = int(0.5*len(x))
posy = int(0.3333333*len(y))

z[posx,posy]=0.5    #Perturbacion
#z[:posx-1,2*posy]=0 #Rendija?
#z[posx+1:,2*posy]=0 #Rendija?

#fig = plt.figure()
#ax = fig.gca(projection ='3d')
#sup = ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap ='copper')
#plt.show()
#plt.close()

z1 = np.zeros((puntos,puntos))
#z1[posx,posy]=0.5
#z1[1:-1,1:-1]=2
for i in range(1,puntos-1):
	for j in range(1, puntos-1):
		z1[i,j] = (z[i,j]+((alpha**2)/2.0)*z[i+1,j]-2*z[i,j]+z[i-1,j])+(z[i,j]+((alpha**2)/2.0)*z[i,j+1]-2*z[i,j]+z[i,j-1])

	
z_past = z
z_actual = z1

z_fut = np.zeros((puntos,puntos))
#z_fut[posx,posy]=0.5
#z_fut[1:-1,1:-1]=2
t = 0

while t<tfinal:
	for i in range(1,puntos-1):
		for j in range(1, puntos-1):
			z_fut[i,j] = 2*(1-alpha**2)*z_actual[i,j]-z_past[i,j]+(alpha**2)*(z_actual[i+1,j]+z_actual[i-1,j])+2*(1-alpha**2)*z_actual[i,j]-z_past[i,j]+(alpha**2)*(z_actual[i,j+1]+z_actual[i,j-1])

	z_past= np.copy(z_actual)
	z_actual = np.copy(z_fut)
	t+=1


fig = plt.figure()
ax = fig.gca(projection ='3d')
sup = ax.plot_surface(X,Y,z_fut,rstride=1,cstride=1,cmap ='copper')
plt.show()
plt.close()










