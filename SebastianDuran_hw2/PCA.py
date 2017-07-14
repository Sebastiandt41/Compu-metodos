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


plt.plot(Tax,c="r", label ="Commercial profits")
plt.plot(GNI,c="g", label = "GNI per capita")
plt.plot(Unemplf , c="b",label= "Female labor force")
plt.plot(Unemplm , c="y",label ="Male labor force")
plt.plot(Ratio , c="c", label = "Ratio f/m labor f" )
plt.legend()
plt.title("Datos economicos banco mundial")
plt.savefig("ExploracionDatos.pdf",format="pdf")
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
plt.title("Datos proyectados")
plt.savefig("PCAdatos.pdf",format="pdf")
plt.close()

#Relacion de las variables

plt.scatter(PC1[0],PC2[0],c="r",marker="o",label="Total tax rate")
plt.scatter(PC1[1],PC2[1],c="b",marker="o",label="Cost of bussines")
plt.scatter(PC1[2],PC2[2],c="y",marker="v",label="Unemployment,female")
plt.scatter(PC1[3],PC2[3],c="g",marker="v",label="Unemployment,male")
plt.scatter(PC1[4],PC2[4],c="c",marker="^",label="Ratio f/m labor force")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(loc=0)
plt.title("Correlacion de variables")
plt.savefig("PCAvariables.pdf",format="pdf")
plt.close()

#Print final 
print "Las variables que esta correlacionadas son : Total tax rate con Cost of business start-up procedures, Y Unemployment-female con Unemployment-male  , mientras que  Ratio of f. to m. labor force participation rate es una variable independiente."





