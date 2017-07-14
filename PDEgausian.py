import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,1,1000)
y = np.exp(-(x-0.3)**2/0.01)

plt.plot(x,y)
plt.show()
plt.close()
