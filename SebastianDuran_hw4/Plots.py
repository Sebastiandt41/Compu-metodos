import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("map_data.txt",delimiter=" ")

print datos[236,217],datos[234,230],datos[62,702],datos[62,703]


plt.imshow(datos)
#circle1  = plt.Circle((327, 123), 100, color='b', fill=False)
plt.plot(123,327,"o")
#plt.plot(x,y)
plt.show()
plt.close()




