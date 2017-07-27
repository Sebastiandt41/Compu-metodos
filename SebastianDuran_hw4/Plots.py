import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("map_data.txt",delimiter=" ")
coordenadas = np.genfromtxt("datos.csv")


centro_x=coordenadas[0]
centro_y=coordenadas[1]
radio = coordenadas[2]
xr = coordenadas[3]
yr = coordenadas[4]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
circ= plt.Circle((xr,yr),radius = radio, color = "r" , fill = False)
ax.set_xlim((0,744))
ax.set_ylim((500,0))
ax.imshow(datos,cmap = "winter",extent=(0,744,500,0))
ax.add_artist(circ)
ax.plot(xr,yr,"o",color = "r")
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
fig.suptitle("Punto Nemo")
plt.savefig("PuntoNemo.pdf")
plt.close()




