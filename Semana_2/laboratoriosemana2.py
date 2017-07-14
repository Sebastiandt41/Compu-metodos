import numpy as np 	
import matplotlib.pyplot as plt
from scipy.stats import expon , norm

alpha = 10

x = np.random.exponential(1*0.1,10000)

#plt.hist(x ,normed = True, bins = 200)
#plt.show()

a,b = expon.fit(x) # Esto bota dos datos, (loc, scale), 1/lamda es la varianza ... en la distribucion normal loc es la varianza

print b 

v = np.linspace(0,1,1000)
w = expon.pdf(v , a , scale = b) 



#plt.plot(v,w)
#plt.show()
#plt.close()

#AHORA OTRA COSITA LOKOOOOOOOOOOASDOASJPGFASIOPGHASG


lista = [] 

i = 0

while i <= 1000:
	k = np.random.exponential(1*0.1,1000) 
	var = np.sum(k)
	lista.append(var)
	i+=1


plt.hist(lista , normed = True , bins = 200)



a2,b2 = norm.fit(lista) #loc(normal es media),varianza (en normal)
print a
#teorema del limite central , pdf = probability density function 
f = np.linspace(0,125,1000)
t = norm.pdf(f,a2,b2)

plt.plot(f,t)
plt.show()








