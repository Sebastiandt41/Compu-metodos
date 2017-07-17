#include <stdlib.h>
#include <stdio.h>

#define g 39.4793 //Unidades en UA y masas solares 

//pasar a masas solares las cosas del archivo

//como vamos a solucionar esta ecuacion diferencial loquete 




int main(void)
{
//primero con dos planetas, ver apuntes 
	FILE *in;
	float m[10];
	float x[10];
	float y[10];
	float z[10];
	float vx[10];
	float vy[10];
	float vz[10]; 
	int i ;
	char archivo[100] = "carol.csv";	
	in = fopen(archivo, "r");	
	for(i=0;i<10;i++)
	{
		fscanf(in, "%f, %f, %f, %f, %f, %f, %f\n", &m[i], &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
		//printf("m= %f\n",m);
	}
	printf("PosicionX = %f\n",x[0]);
	printf("PosicionY = %f\n",y[0]);
	fclose(in);
	return 0;
	
	
}
	/*//distancias en AU 
	float masa;
	float posx[100];
	float posy[];
	float posz[100];
	float vx[100];
	float vy[100];
	float vz[100];
	
	int condiciones1[7];
	int condiciones2[7];
	
	float pos_solx = 0;
	float pos_soly = 0;	
	float pos_solz = 0;
	//en la realidad es del archivo 
	posx[0] = 13;
	posy[0] = 15;
	posz[0] = 25;
	vx[0] = 0;
	vy[0] = 0;
	vz[0] = 0;
	//Llamo la funcion que calcula la aceleracion 
	
	return 0;
	*/



	
