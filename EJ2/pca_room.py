import numpy as np
import matplotlib.pyplot as plt 

datos= np.genfromtxt("room-temperature.csv",delimiter =',',skip_header = 1, usecols = (1,2,3,4))

T1 = datos[:,0]
T2 = datos[:,1]
T3 = datos[:,2]
T4 = datos[:,3]

#Figura de temperaturas

fig, temperatures = plt.subplots(4,1)
temperatures [0].plot(T1,color = 'r')
temperatures [0].set_ylabel('T1')
temperatures [1].plot(T2,color = 'r')
temperatures [1].set_ylabel('T2')
temperatures [2].plot(T3,color = 'r')
temperatures [2].set_ylabel('T3')
temperatures [3].plot(T4,color = 'r')
temperatures [3].set_xlabel('Tiempo')
temperatures [3].set_ylabel('T4')
plt.suptitle('Temperaturas')
plt.savefig("temp.png",format ='png')
plt.close()

#Centrar y normalizar los datos 

T_1= ((T1-np.mean(T1))/np.std(T1))
T_2= ((T2-np.mean(T2))/np.std(T2))
T_3= ((T3-np.mean(T3))/np.std(T3))
T_4= ((T4-np.mean(T4))/np.std(T4))

#Matriz de covarianza
matriz =[T_1,T_2,T_3,T_4]
covarianza_temp = np.cov(matriz)
print covarianza_temp

#Eigenvalores y Eigenvectores
eig_val = np.linalg.eig(covarianza_temp)
v = eig_val[0]
vectores = eig_val[1]
print  "La primera componente principal es " ,vectores[0] , "con valor" , v[0]
print  "La segunda componente principal es " ,vectores[1] , "con valor" , v[1]

#Contribucion a la varianza de las primeras dos componentes 

suma_v = 0
for elemento in v:
	suma_v+= elemento

VAR_1 = (v[0]*100.0)/suma_v
VAR_2 = (v[1]*100.0)/suma_v

print "La primera componente principal explica el",VAR_1,"% de la varianza"
print "La segunda componente principal explica el",VAR_2,"% de la varianza"


#Graficar Front Right vs Front Left , Back Left vs Front Left

VECTOR1 = vectores[:,0]
VECTOR2 = vectores[:,1]

m11= VECTOR1[1]/VECTOR1[0]
m12= VECTOR2[1]/VECTOR2[0]

m21 = VECTOR1[2]/VECTOR1[0]
m22 = VECTOR2[2]/VECTOR2[0]


puntos = np.linspace(-4,4,100)

y11 = puntos*m11
y12 = puntos*m12


y21 = puntos*m21
y22 = puntos*m22

#Front Right vs Front Left
plt.scatter(T_1,T_2)
plt.plot(puntos,y11,label="PC1")
plt.plot(puntos,y12,label="PC2")
plt.title("PCA Front Right vs Front Left")
plt.xlabel("Front Left Temperature")
plt.ylabel("Front Right Temperature")
plt.legend(loc=0)
plt.savefig("pca_fr_fl.pdf",format='pdf')
plt.close()

#Back Left vs Front Left
plt.scatter(T_1,T_3)
plt.plot(puntos,y21,label="PC1")
plt.plot(puntos,y22,label="PC2")
plt.title("PCA Back Left vs Front Left")
plt.xlabel("Front Left Temperature")
plt.ylabel("Back Left Temperature")
plt.legend(loc=0)
plt.savefig("pca_bl_fl.pdf",format='pdf')
plt.close()























