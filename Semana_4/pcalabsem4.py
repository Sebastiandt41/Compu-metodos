import numpy as np
import matplotlib.pyplot as plt 

food = np.loadtxt("food-texture.csv",skiprows = 1, usecols=[1,2,3,4,5],delimiter=",")

#fig,textures = plt.subplots(5,1)
#textures[0].hist(food[:,0])
#textures[1].hist(food[:,1])
#textures[2].hist(food[:,2])
#textures[3].hist(food[:,3])
#textures[4].hist(food[:,4])
#plt.show()
#plt.savefig("food.jpg")
plt.close

#Vamos a escalar los datos , a cada dato le resto la media y lo divido en la desviacion estandar,entre menos 2 y dos 

food_0 = (food[:,0]-np.mean(food[:,0]))/np.std(food[:,0])
food_1 = (food[:,1]-np.mean(food[:,1]))/np.std(food[:,1])
food_2 = (food[:,2]-np.mean(food[:,2]))/np.std(food[:,2])
food_3 = (food[:,3]-np.mean(food[:,3]))/np.std(food[:,3])
food_4 = (food[:,4]-np.mean(food[:,4]))/np.std(food[:,4])

#fig,textures = plt.subplots(5,1)
#textures[0].hist(food_0)
#textures[1].hist(food_1)
#textures[2].hist(food_2)
#textures[3].hist(food_3)
#textures[4].hist(food_4)
#plt.show()
plt.close()

matriz = [food_0,food_1,food_2,food_3,food_4]
covarianza_food = np.cov(matriz)

eig_val = np.linalg.eig(covarianza_food)
v = eig_val[0]
vectores = eig_val[1]
print  vectores

#Calcular el porcentaje de cada valor propio en la suma total de los valores propios 60,25,6,4.8,2..

plt.scatter(food_3,food_4)



vector_1 = vectores[:,0]
vector_2 = vectores[:,1]
vector_3 = vectores[:,2]
vector_4 = vectores[:,3]
vector_5 = vectores[:,4]

m1 = vector_1[3]/vector_1[4]
m2 = vector_2[3]/vector_2[4]


x1 = np.linspace(-2,2,10)

y1 = x1*m1
y2 = x1*m2


plt.plot(x1,y1)
plt.plot(x1,y2)

#la primera posicion del vector propio se refiere a la primera variable , la segunda a la segunda , la tercera  a la tercera y asi....


plt.show()
plt.close()




















