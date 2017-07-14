import numpy as np 
import matplotlib.pyplot as plt

#Crea el espacio 
def generar_espacio():
	x1 = np.linspace(-1.0,1.0,150)
	y1 = np.linspace(-1.0,1.0,150)
	xx,yy = np.meshgrid(x1,y1)
	return xx,yy

#Calcula la distancia entre los puntos del espacio
def calcdist():
	x1 = np.linspace(-1.0,1.0,150)
	y1 = np.linspace(-1.0,1.0,150)
	h = x1[2]-x1[1]
	return h

#Clase carga
class Carga: 
	
	k1 = 8.987*10**9 # unidades en N, m, C 
	e = 1.602176*10**-19 #unidades en C 
	k = 0.230693541 # unidades en kg , nm , e y s 

	#Constructor de la clase 
	def __init__(self,x0,y0,q0):
		self.x=x0
		self.y=y0
		self.q=q0
	#Retorna el potencial de la carga
	def calcV (self):		
		xx,yy = generar_espacio()		
		self.potencial = (self.k*self.q)/(np.sqrt((xx-(self.x))**2 + (yy-(self.y))**2)+0.1)				
		return self.potencial
	#Retorna la derivada parcial del potencial con respecto a x (algoritmo de central difference)
	def calcdvdx(self):		
		x1,y1 = generar_espacio()
		h = calcdist()
		dx1 = (self.k*self.q)/(np.sqrt(((x1+(h*0.5))-(self.x))**2 + ((y1)-(self.y))**2))
		dx2 = (self.k*self.q)/(np.sqrt(((x1-(h*0.5))-(self.x))**2 + ((y1)-(self.y))**2))
		dvdx = (dx1 - dx2)/h		
		return dvdx
	#Retorna la derivada parcial del potencial con respecto a y (algoritmo de central difference)
	def calcdvdy(self):
		x1,y1 = generar_espacio()
		h = calcdist()
		dy1 = (self.k*self.q)/(np.sqrt(((x1)-(self.x))**2 + ((y1+(h*0.5))-(self.y))**2))
		dy2 = (self.k*self.q)/(np.sqrt(((x1)-(self.x))**2 + ((y1-(h*0.5))-(self.y))**2))
		dvdy = (dy1 - dy2)/h		
		return dvdy

X,Y = generar_espacio()

carga1 = Carga(-0.5,0.5,-1)
carga2 = Carga(0.5,0.5,1)
carga3 = Carga(0.5,-0.5,-1)
carga4 = Carga(-0.5,-0.5,1)

#Potencial debido a las 4 cargas
PotencialTotal= carga4.calcV()+carga3.calcV()+carga2.calcV()+carga1.calcV()
#Componente x del campo electrico debido a las cargas 
Ex = -(carga4.calcdvdx()+carga3.calcdvdx()+carga2.calcdvdx()+carga1.calcdvdx())
#Componente y del campo electrico debido a las cargas 
Ey = -(carga4.calcdvdy()+carga3.calcdvdy()+carga2.calcdvdy()+carga1.calcdvdy())

#Guarda la figura con el potencial y las lineas de campo electrico obtenidos numericamente
plt.streamplot(X,Y,Ex,Ey,linewidth = 1,color='b')
plt.imshow(PotencialTotal,extent=(-1.0,1.0,-1.0,1.0),origin = 'lower', cmap='hot')
plt.colorbar(orientation='vertical')
plt.title("Potencial y Campo electrico")
plt.xlabel("nm")
plt.ylabel("nm")
plt.savefig("cargas.pdf",format = 'pdf')





	
























