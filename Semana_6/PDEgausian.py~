import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,1,1000)
y0 = np.exp(-(x-0.3)**2/0.01)
delta_t = 0.0005
delta_x = 1.0/999
c = 1.0 
gamma = c*(delta_t/delta_x)
plt.plot(x,y0)
plt.show()
plt.close()

y1 = np.zeros(1000)
y1[0] = 0
y1[-1]= 0
for i in range(1,999):
	y1[i] = y0[i]+((gamma**2)/2.0)*(y0[i+1]-2*y0[i]+y0[i-1])

plt.plot(x,y1)
plt.show()
plt.close()

y2 = np.zeros(1000)
y2[0] = 0
y2[-1] = 0
for i in range(1,999):
	y2[i] =2*(1-gamma**2)*y1[i]-y0[i]+(gamma**2)*(y1[i+1]+y1[i-1])

plt.plot(x,y2)
plt.show()
plt.close()

y_past = y0
y_actual = y1
y_fut = np.zeros(1000)
i = 0
while i < 350:		
	for j in range(1,999):
		y_fut[j] = 2*(1-gamma**2)*y_actual[j]-y_past[j]+(gamma**2)*(y_actual[j+1]+y_actual[j-1])
	y_past = np.copy(y_actual)	
	y_actual = np.copy(y_fut)
	i+=1	

plt.plot(x,y_fut)
plt.show()
plt.close()
	













