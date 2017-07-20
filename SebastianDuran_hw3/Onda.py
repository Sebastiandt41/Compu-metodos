import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation


damn = 80.0
puntos = int(damn)
a = 0.0
b = 30.0
c = 1.0
x = np.linspace(a,b,puntos)
y = np.linspace(a,b,puntos)
nu = 1.0
sigma = 0.3
dx = (b-a)/(damn-1.0)
dy = (b-a)/(damn-1.0)
alpha = 0.5
dt = np.sqrt(0.5)*dx**2
z = np.zeros((puntos,puntos))
X,Y = np.meshgrid(x,y)
n= 60.0/dt
n1=int(n)


posx = int(0.5*len(x))
posy = int(0.3333333*len(y))

#z[1:-1,1:-1]=2.0*np.exp(-((x-posx)**2/0.01+(y-posy)**2/0.01))
#z[:,:]=-0.5*np.exp(-(((x-posx)**2/2*0.01)+((y-posy)**2/2*0.01)))
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
#z1[:,:]=2.0*np.exp(-((x-posx)**2/0.01+(y-posy)**2/0.01))
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
while t<n1:
	#z_actual[posx,posy]=-0.5
	#z_actual[:,:]=2.0*np.exp(-((x-posx)**2/0.01+(y-posy)**2/0.01))
	for i in range(1,puntos-1):
		for j in range(1, puntos-1):
			z_fut[i,j] = 2*z_actual[i,j]-z_past[i,j]+alpha*(z_actual[i+1,j]-2*z_actual[i,j]+z_actual[i-1,j])+alpha*(z_actual[i,j+1]-2*z_actual[i,j]+z_actual[i,j-1])
	z_fut[0,:]=0
	z_fut[-1,:]=0
	z_fut[:,0]=0
	z_fut[:,-1]=0
	z_fut[:posx-4,2*posy]=0#Rendija
	z_fut[posx+4:,2*posy]=0 #Rendija
	
	z_past= np.copy(z_actual)
	z_actual = np.copy(z_fut)
	estados.append(z_actual)
	t+=1

t30 = int(30.0/dt)
t60 = int(60.0/dt)

fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')
sup = ax.plot_surface(X,Y,estados[t30],rstride=2,cstride=2,cmap = "seismic")
fig.colorbar(sup,shrink=0.5,aspect=5)
ax.set_zlim(-1,1)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$phi$")
plt.savefig("Onda3D_t30.png")
#plt.show()
plt.close()

plt.imshow(estados[t30],cmap = "seismic")
plt.colorbar()
plt.savefig("Onda2D_t30.png")
#plt.show()
plt.close()

fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')
sup = ax.plot_surface(X,Y,estados[t60],rstride=2,cstride=2,cmap = "seismic")
fig.colorbar(sup,shrink=0.5,aspect=5)
ax.set_zlim(-1,1)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$phi$")
plt.savefig("Onda3D_t60.png")
#plt.show()
plt.close()

plt.imshow(estados[t60],cmap = "seismic")
plt.colorbar()
plt.savefig("Onda2D_t60.png")
#plt.show()
plt.close()

#figu,ax = plt.subplots()


def animar(i):
	ax.clear()
	ax.set_zlim(-1,1)
	estado = estados[i]	
	sup = ax.plot_surface(X,Y,estado,rstride=1,cstride=1,cmap = "seismic")		
	return sup,

#ani = animation.FuncAnimation(fig,animar,n1,interval=5,blit=False)
#ani.save("Onda.mp4",writer="ffmpeg",fps=14)
#plt.show()
#plt.close()

	
	

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





