import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation


puntos = 60
a = 0.0
b = 30
c = 1.0
x = np.linspace(a,b,puntos)
y = np.linspace(a,b,puntos)
tfinal = 120

nu = 1.0
sigma = 0.3
dx = b-a/puntos-1.0
dy = b-a/puntos-1.0
dt = sigma*dx**2/c
#alpha = (c*dt**2)/dx**2
alpha = 0.5
z = np.zeros((puntos,puntos))
X,Y = np.meshgrid(x,y)
#z =


#print z[:,0],z[0,:],z[:,-1],z[-1,:]

posx = int(0.5*len(x))
posy = int(0.3333333*len(y))

#z[1:-1,1:-1]=2.0*np.exp(-((x-posx)**2/0.01+(y-posy)**2/0.01))
z[:,:]=2.0*np.exp(-((x-posx)**2/2*dx**2+(y-posy)**2/2*dy**2))
z[posx,posy]=-0.5    #Perturbacion
z[0,:]=0
z[-1,:]=0
z[:,0]=0
z[:,-1]=0
#z[:posx-1,2*posy]=0 #Rendija?
#z[posx+1:,2*posy]=0 #Rendija?

#fig = plt.figure()
#ax = fig.gca(projection ='3d')
#sup = ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap ='copper')
#plt.show()
#plt.close()

z1 = np.zeros((puntos,puntos))
z1[:,:]=2.0*np.exp(-((x-posx)**2/0.01+(y-posy)**2/0.01))
z1[posx,posy]=-0.5
#z1[1:-1,1:-1]=2
for i in range(1,puntos-1):
	for j in range(1, puntos-1):
		z1[i,j] = z[i,j]+alpha*(z[i+1,j]-2*z[i,j]+z[i-1,j])+alpha*(z[i,j+1]-2*z[i,j]+z[i,j-1])
z1[0,:]=0
z1[-1,:]=0
z1[:,0]=0
z1[:,-1]=0
	
z_past = np.copy(z)
z_actual = np.copy(z1)

z_fut = np.zeros((puntos,puntos))
z_fut[posx,posy]=-0.5
#z_fut[1:-1,1:-1]=2
t = 0
estados =[]
estados.append(z)
estados.append(z1)

#def pard():
while t<tfinal:
	#z_actual[posx,posy]=-0.5
	#z_actual[:,:]=2.0*np.exp(-((x-posx)**2/0.01+(y-posy)**2/0.01))
	for i in range(1,puntos-1):
		for j in range(1, puntos-1):
			z_fut[i,j] = 2*z_actual[i,j]-z_past[i,j]+alpha*(z_actual[i+1,j]-2*z_actual[i,j]+z_actual[i-1,j])+alpha*(z_actual[i,j+1]-2*z_actual[i,j]+z_actual[i,j-1])
	z_fut[0,:]=0
	z_fut[-1,:]=0
	z_fut[:,0]=0
	z_fut[:,-1]=0
	#z_fut[:,0]=z_fut[:,1]
	#z_fut[:,puntos-1]=z_fut[:,puntos-2]
	#z_fut[0,:]=z_fut[1,:]
	#z_fut[puntos-1,:]=z_fut[puntos-2,:]
	z_past= np.copy(z_actual)
	z_actual = np.copy(z_fut)
	estados.append(z_actual)
	t+=1
	#return z_actual

#fig = plt.figure()
#ax = fig.add_subplot(111,projection ='3d')
#sup, = ax.plot([],[],[])

#def animar(i):
#	sup.set_data(X,Y,estados[i])
#	return sup,
#ani = animation.FuncAnimation(fig,animar,tfinal,interval = 25, blit=True)
#ani.save("Ondas.gif",writer="imagemagick")
#plt.show()
#plt.close()

fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')
sup = ax.plot_surface(X,Y,estados[15],rstride=1,cstride=1,cmap ='summer')
fig.colorbar(sup,shrink=0.5,aspect=5)
ax.set_zlim(-0.3,0.3)
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()
plt.close()

def animar(i):
	estado = estados[i]
	ax.clear()
	sup = ax.plot_surface(X,Y,estado,rstride=1,cstride=1,cmap ='summer')
	ax.set_zlim(-0.3,0.3)	
#ax.set_zlim(-2.5,2.5)	
	return sup,

ani = animation.FuncAnimation(fig,animar,tfinal,interval=25,blit=False)
ani.save("Oonndsif1.mp4",writer="ffmpeg",fps=15)
plt.show()
plt.close()

	
	







