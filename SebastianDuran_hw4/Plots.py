import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("map_data.txt",delimiter=" ")
coordenadas = np.genfromtxt("datos.csv")

radio = coordenadas[0]
xr = coordenadas[1]
yr = coordenadas[2]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
circ= plt.Circle((xr,yr),radius = radio, color = "r" , fill = False)
ax.imshow(datos)
ax.add_artist(circ)
ax.plot(xr,yr,"o",label ="Punto nemo")
plt.legend()
plt.show()
plt.close()




