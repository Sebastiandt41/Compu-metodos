import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,1,1000)
y = np.exp(-(x-0.3)**2/0.01)
delta_t = 0.0005
delta_x = 1.0/999
c = 1.0 
gamma = c*(delta_t/delta_x)
plt.plot(x,y)
plt.show()
plt.close()

u = np.zeros(1000)
u[0] = 0
u[-1]= 0
for i in range(1,999):
	u[i] = y[i]+((gamma**2)/2.0)*(y[i+1]-2*y[i]+y[i-1])

plt.plot(x,u)
plt.show()
plt.close()

