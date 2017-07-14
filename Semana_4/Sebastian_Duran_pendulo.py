import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

#a = 0
#b = np.pi
h = 0.01
n = 1000
g = 9.8
l = 1

#h = float((b-a)/(n-1.0))	
#n = int(((b-a)/h)+1)
t = np.zeros(n)
theta_1 = np.zeros(n)
theta_2 = np.zeros(n)
#Implementacion de la ecuacion diferencial 
def func_prime_1(t,theta_1,theta_2):
	return theta_2 

def func_prime_2(t,theta_1,theta_2):
	return -(g/l)*(np.sin(theta_1))
	 
#Condiciones iniciales
t[0] = 0.0
theta_1[0] = np.pi*0.25
theta_2[0] = 0.0

#Derivadas

for i in range(1,n):
	theta_1[i] = func_prime_1(t[i-1],theta_1[i-1],theta_2[i-1])
	theta_2[i] = func_prime_2(t[i-1],theta_1[i-1],theta_2[i-1])
	
	t[i] = t[i-1]+h
	theta_1[i] = theta_1[i-1]+h * func_prime_1(t[i-1],theta_1[i-1],theta_2[i-1])
	theta_2[i] = theta_2[i-1]+h * func_prime_2(t[i-1],theta_1[i-1],theta_2[i-1])


#plt.plot(t,theta_1)
#plt.xlabel('t')
#plt.ylabel('theta(t)')
#plt.show()
#plt.close()

#Cambio de coordenadas 

X = l*np.sin(-theta_1)
Y = -l*np.cos(theta_1)

#Animacion 

fig, ax = plt.subplots()
line, = ax.plot([],[],"-o")

def animar(i):
    line.set_data([0,X[i]],[0,Y[i]])  # update the data
    return line,


ani = animation.FuncAnimation(fig, animar, len(X) , 
                              interval=25, blit=True)
ax.set_title("Pendulo")
ax.set_xlim(-l,l)
ax.set_ylim(-l,l)
plt.show()









