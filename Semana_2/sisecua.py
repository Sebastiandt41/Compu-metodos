#Sistemas de ecuaciones lineales 
import numpy as np

matriz = [[5.0,7.0,3.0,1.0],[3.0,6.0,5.0,3.0],[6.0,7.0,8.0,6.0],[3.0,4.5,6.5,2.7]]

b= [2.0,3.0,5.0,7.0]

x = np.array(matriz)

matrix = np.matrix(x)

m = len(matrix[0])
n = len(matrix[:,0])



#Segun julioprofe el orden para reducir la matriz a ceros primero es 31,21,32,13,23,12

#for i in range(m):

def resolversistema():

	if matrix[0,0] !=0:
		if matrix[2,0]<0:
			matrix[2,0] = matrix[2,0]+(matrix[0,0]*matrix[2,0])
		else:
			matrix[2,0] = matrix[2,0]-(matrix[0,0]*matrix[2,0])

	print matrix

def resolversistema2():
	if matrix[0,0] != 0:
		matrix[0,:]= matrix[0,:]/matrix[0,0]
		matrix[1] = matrix[1] - (matrix[0]*matrix[1,0])
		matrix[1,:]= matrix[1,:]/matrix[1,1]
		matrix[2] = matrix[2] - (matrix[0]*matrix[2,0])
		matrix[2] = matrix[2] - (matrix[1]*matrix[2,1])
		matrix[2] = matrix[2,:]/matrix[2,2]
		matrix[3] = matrix[3] - (matrix[0]*matrix[3,0])
		matrix[3] = matrix[3] - (matrix[1]*matrix[3,1])
		matrix[3] = matrix[3] - (matrix[2]*matrix[3,2])
		matrix[3] = matrix[3,:]/matrix[3,3]
	print matrix 



dim = np.size(matrix[:,0])

def resolversistema3():

	if matrix[0,0] != 0 and (np.size(matrix[0,:]) == np.size(matrix[:,0])):
		for i in range(0,dim):
			for j in range(0,dim):

				if i > j:
					matrix[i] = matrix[i] - (matrix[j]*matrix[i,j])
					b[i] = b[i] - (b[i]*matrix[i,j])
				
				
				elif i == j:
					matrix[i] = matrix[i]/matrix[i,j]
					#b[i] = b[i]/matrix[i,j]
	return matrix , b 
	
				


print resolversistema3()









#No olvidar el B , y hacerle los mismos pasos en el for 
		
 	







