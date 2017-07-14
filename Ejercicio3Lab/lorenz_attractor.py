import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Constantes

h = 0.01
sigma=10.0
ro = 28.0
beta = 8.0/3.0
n = int((40/0.01)+1.0)
t = np.linspace(0,40,n)

print n

#Arrays

x = np.zeros(n)
x1 = np.zeros(n)
y =np.zeros(n)
y1 =np.zeros(n)
z =np.zeros(n)
z1 =np.zeros(n)

x[0]=1.0
y[0]=1.0
z[0]=1.0
x1[0]= sigma*(y[0]-x[0])
y1[0]= x[0]*(ro-z[0])-y[0]
z1[0]= x[0]*y[0]-beta*z[0]

#derivada

for i in range (1,n):
	x[i] = x1[i-1]*h +x[i-1]
	y[i] = y1[i-1]*h +y[i-1]
	z[i] = z1[i-1]*h +z[i-1]
	x1[i] = sigma*(y[i]-x[i])
	y1[i]= x[i]*(ro-z[i])-y[i]
	z1[i]= x[i]*y[i]-beta*z[i]
	
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z)
fig.suptitle("Lorenz attractor")
plt.savefig("lorenz.png",format="png")
plt.close()

	
























