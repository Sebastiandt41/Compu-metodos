import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("map_data.txt",delimiter=" ")
coordenadas = np.genfromtxt("datos.csv")



radio = coordenadas[2]
xr = coordenadas[3]
yr = coordenadas[4]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
circ= plt.Circle((xr,yr),radius = radio, color = "r" , fill = False)
ax.imshow(datos,cmap = "winter")
ax.add_artist(circ)
ax.plot(xr,yr,"o",label ="Punto nemo",color = "k")
#plt.legend()
plt.savefig("PuntoNemo.pdf")
plt.show()
plt.close()




