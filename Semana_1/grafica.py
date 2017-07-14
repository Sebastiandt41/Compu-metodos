
import numpy as np 
import matplotlib.pyplot as plt

plt.figure('scatter') 
 

a = np.random.rand(50) 
b = np.random.rand(50)

plt.figure('scatter')

plt.scatter(a,b) 
plt.savefig('background', format='pdf')
plt.savefig('imagen', format ='png')
plt.show()


