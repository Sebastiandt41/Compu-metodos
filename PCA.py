import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

datos = pd.read_csv("DatosBancoMundial5.csv",sep=",")
datos_1 = datos.as_matrix()
datos_2 = datos_1[:,4:]

Tax_rate = datos_2[0]
GNI_perC = datos_2[1]
Unempl_fem = datos_2[2]
Unempl_mal = datos_2[3]
Ratio_fem_mal = datos_2[4]

#Normalizacion de los datos

Tax = ((Tax_rate-np.mean(Tax_rate))/np.std(Tax_rate))
GNI = ((GNI_perC-np.mean(GNI_perC))/np.std(GNI_perC))
Unemplf = ((Unempl_fem-np.mean(Unempl_fem))/np.std(Unempl_fem))
Unemplm = ((Unempl_mal -np.mean(Unempl_mal))/np.std(Unempl_mal))
Ratio = ((Ratio_fem_mal-np.mean(Ratio_fem_mal))/np.std(Ratio_fem_mal))


#Grafica 1 

fig,var = plt.subplots(5,1)
var[0].plot(Tax,c="r", label = "Total tax rate")
var[0].legend()
var[1].plot(GNI,c="g", label = "Cost of business")
var[1].legend()
var[2].plot(Unemplf , c="b",label= "Unemployment,female")
var[2].legend()
var[3].plot(Unemplm , c="y",label =" Unemployment,male")
var[3].legend()
var[4].plot(Ratio , c="c", label = "Ratio of f. to m. labor force participation rate" )
var[4].legend()
plt.suptitle("Datos economicos banco mundial")
#plt.savefig("Exploracion_Datos.pdf",format="pdf")
plt.show()
plt.close()

#Matriz de covarianza 

matriz = [Tax,GNI,Unemplf,Unemplm,Ratio]
matriz_1 = np.transpose(matriz)

n = len(matriz) 
M = len(matriz[0])

Cov = np.identity(n)


for i in range(n):
	for j in range(n):
		b= 0
		for k in range(M):				
			b += (matriz_1[k,i]-np.mean(matriz_1[:,i]))*(matriz_1[k,j]-np.mean(matriz_1[:,j]))/(M-1)
		
		Cov[i][j] = b

#Eigenvalores y Eigenvectores
eig_val = np.linalg.eig(Cov)
v = eig_val[0]
vectores = eig_val[1]

PC1 = vectores[:,0]
PC2 = vectores[:,1]

print "El componente principal es:",PC1,",el segundo componente principal es:",PC2

#Proyeccion

proyeccion =np.dot(np.transpose(vectores), matriz)
plt.scatter(proyeccion[0,:],proyeccion[1,:])
plt.xlabel("PC1")
plt.ylabel("PC2")
#plt.savefig("PCAdatos.pdf",format="pdf")
plt.show()
plt.close()

#Relacion de las variables

plt.scatter(PC1[0],PC2[0],label="% of commercial profits")
plt.scatter(PC1[1],PC2[1],label="% of GNI per capita")
plt.scatter(PC1[2],PC2[2],label="% of female labor force")
plt.scatter(PC1[3],PC2[3],label="% of male labor force")
plt.scatter(PC1[4],PC2[4],label="Ratio of f. to m. labor force participation rate %")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(loc=0)
#plt.savefig("PCAvariables.pdf",format="pdf")
plt.show()
plt.close()

#Print final 
print "The variables that are related based on the data of the world bank are : Total tax rate & Cost of business start-up procedures and Unemployment,female & male , while Ratio of f. to m. labor force participation rate is an independent variable."








