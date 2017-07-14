import numpy as np 
import matplotlib.pyplot as plt

#Lectura de datos 
datos = np.genfromtxt("room-temperature.csv",usecols = (1,2,3,4),delimiter =',',skip_header = 1)

Temp1 = datos[:,0]
Temp2 = datos[:,1]
Temp3 = datos[:,2]
Temp4 = datos[:,3]

#Normalizacion de datos 
Temp1= ((Temp1-np.mean(Temp1))/np.std(Temp1))
Temp2= ((Temp2-np.mean(Temp2))/np.std(Temp2))
Temp3= ((Temp3-np.mean(Temp3))/np.std(Temp3))
Temp4= ((Temp4-np.mean(Temp4))/np.std(Temp4))

matriz =[Temp1,Temp2,Temp3,Temp4]

#Matriz de covarianza
covarianza_temp = np.cov(matriz)

#Autovalores y autovectores
eig_val = np.linalg.eig(covarianza_temp)
valores = eig_val[0]
vectores = eig_val[1]

PC1 = vectores[:,0]
PC2 = vectores[:,1]

print "PC1  es " , PC1 , "y PC2 es ", PC2


#Agrupaciones  

plt.scatter(PC1[0],PC2[0],c="r",marker = "v",label="T1-Front left")
plt.scatter(PC1[1],PC2[1],c="b",marker = "v",label="T2-Front right")
plt.scatter(PC1[2],PC2[2],c="g",marker = "^",label="T3-Back left")
plt.scatter(PC1[3],PC2[3],c="y",marker = "^",label="T4-Back right")
plt.legend()
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.xlim([-1,1])
plt.title("Agrupaciones")
plt.savefig("Agrupaciones.pdf",format="pdf")
plt.close()




















