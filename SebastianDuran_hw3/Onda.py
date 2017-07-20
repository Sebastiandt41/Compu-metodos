import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation

#Constantes

dim = 300.0
puntos = int(dim)
a = 0.0
b = 30.0
c = 1.0
dx = (b-a)/(dim-1.0)
dy = (b-a)/(dim-1.0)
alpha = 0.5
dt = (np.sqrt(0.5)*dx)/c**2
n= 60.0/dt
n1=int(n)

#Espacio

x = np.linspace(a,b,puntos)
y = np.linspace(a,b,puntos)
X,Y = np.meshgrid(x,y)
z = np.zeros((puntos,puntos))

#Posicion de la perturbacion

posx = int((1.0/3.0)*len(y))
posy = int(0.5*len(x))

#Condiciones iniciales 

z[posx,posy]=-0.5    #Perturbacion
z[0,:]=0
z[-1,:]=0
z[:,0]=0
z[:,-1]=0
z[2*posx,:posy-8]=0 #Rendija
z[2*posx,posy+8:]=0 #Rendija

#Condiciones iniciales para n=0

z1 = np.zeros((puntos,puntos))
z1[posx,posy]=-0.5
z1[0,:]=0
z1[-1,:]=0
z1[:,0]=0
z1[:,-1]=0
z1[2*posx,:posy-8]=0 #Rendija
z1[2*posx,posy+8:]=0 #Rendija

#Solucion de la ecuacion de onda en dos dimensiones mediante el metodo de diferencias finitas para n=1
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


nn = 0
estados =[]
estados.append(z)
estados.append(z1)


while nn <n1:
	
	for i in range(1,puntos-1):
		for j in range(1, puntos-1):
			z_fut[i,j] = 2*z_actual[i,j]-z_past[i,j]+alpha*(z_actual[i+1,j]-2*z_actual[i,j]+z_actual[i-1,j])+alpha*(z_actual[i,j+1]-2*z_actual[i,j]+z_actual[i,j-1])
	z_fut[0,:]=0
	z_fut[-1,:]=0
	z_fut[:,0]=0
	z_fut[:,-1]=0
	z_fut[2*posx,:posy-8,]=0#Rendija
	z_fut[2*posx,posy+8:]=0#Rendija
	
	z_past= np.copy(z_actual)
	z_actual = np.copy(z_fut)
	estados.append(z_actual)
	nn+=1

t30 = int(30.0/dt)
t60 = int(60.0/dt)

#Grafica para t = 30 en 3D , cstride y rstride dependen de dim (para dim = 100, r-cstride = 2, para dim = 300, r-cstride = 8)
fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')
sup = ax.plot_surface(X,Y,estados[t30],rstride=8,cstride=8,cmap = "seismic")
cb = fig.colorbar(sup,shrink=0.5,aspect=5)
cb.set_label("Amplitud")
ax.set_zlim(-2,2)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$phi$")
ax.set_zlim(-0.5,0.5)
plt.title("t = $30s$" )
plt.savefig("Onda3D_t30.png")
plt.close()

#GRafica para t= 30 en 2D
plt.imshow(estados[t30],cmap = "seismic",extent=(0,30,0,30))
cb = plt.colorbar(sup,shrink=0.5,aspect=5)
cb.set_label("Amplitud")
plt.title("t = $30s$" )
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("Onda2D_t30.png")
plt.close()

#Grafica para t = 60 en 3D , cstride y rstride dependen de dim (para dim = 100, r-cstride = 3, para dim = 300, r-cstride = 8)
fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')
sup = ax.plot_surface(X,Y,estados[t60],rstride=8,cstride=8,cmap = "seismic")
cb = fig.colorbar(sup,shrink=0.5,aspect=5)
cb.set_label("Amplitud")
ax.set_zlim(-2,2)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$phi$")
ax.set_zlim(-0.5,0.5)
plt.title("t = $60s$" )
plt.savefig("Onda3D_t60.png")
plt.close()


#GRafica para t= 60 en 2D
plt.imshow(estados[t60],cmap = "seismic",extent=(0,30,0,30))
cb = plt.colorbar(sup,shrink=0.5,aspect=5)
cb.set_label("Amplitud")
plt.title("t = $60s$" )
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("Onda2D_t60.png")
plt.close()


#Estado inicial para la animacion en 2D
figu , ax = plt.subplots()
im = plt.imshow(estados[0],cmap = "seismic")
cb = plt.colorbar(sup,shrink=0.5,aspect=5)
cb.set_label("Amplitud")


#Funcion para animar la onda en dos dimensiones 
def animar_bien(i):
	ax.clear()
	estado = estados[i]
	im = plt.imshow(estado,cmap="seismic",extent=(0,30,0,30))
	ax.set_xlabel(r"$x$")
	ax.set_ylabel(r"$y$")
	plt.title("Onda 2D")
		
	return im

#Crea la animacion en 2D y la guarda
ani_imshow = animation.FuncAnimation(figu,animar_bien,n1,interval = 40,blit = False)
ani_imshow.save("Onda.mp4",writer = "ffmpeg",fps = 15 ,dpi = 50)
plt.close()	

#Estado inicial para la animacion en 3D
figx = plt.figure()
ax1 = figx.add_subplot(111,projection ='3d')
sup = ax1.plot_surface(X,Y,estados[0],rstride=8,cstride=8,cmap = "seismic")
cb = figx.colorbar(sup,shrink=0.5,aspect=5)
cb.set_label("Amplitud")


#Funcion para animar la onda en tres dimensiones 
def animar(i):
	ax1.clear()
	estado = estados[i]	
	sup = ax1.plot_surface(X,Y,estado,rstride=8,cstride=8,cmap = "seismic")	
	plt.title("Onda 3D")	
	ax1.set_xlabel(r"$x$")
	ax1.set_ylabel(r"$y$")
	ax1.set_zlabel(r"$phi$")
	ax1.set_zlim(-0.5,0.5)
	return sup,

#Crea la animacion en 3D y la guarda
#ani = animation.FuncAnimation(figx,animar,n1,interval=30,blit=False)
#ani.save("Onda3D.mp4",writer="ffmpeg",fps= 15)
#plt.close()




	







