#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define g 39.4793 //Unidades en UA y masas solares 

//pasar a masas solares las cosas del archivo

//como vamos a solucionar esta ecuacion diferencial loquete 

//10 AÑOS CON DT 0.01 SON 10000 POSICIONES , LUEGO SON 250 AÑOS CREO PARA LA VUELTA COMPLETA

int inde(int i,int j);
int main(void)
{
//primero con dos planetas, ver apuntes 
	FILE *in;

	/*float m[10];
	float x[10];
	float y[10];
	float z[10];
	float vx[10];
	float vy[10];
	float vz[10]; 
	*/
	float m[10];
	float *x = malloc((10*10000)*sizeof(float));
	float *y = malloc((10*10000)*sizeof(float));
	float *z = malloc((10*10000)*sizeof(float));
	float *vx = malloc((10*10000)*sizeof(float));
	float *vy = malloc((10*10000)*sizeof(float));
	float *vz = malloc((10*10000)*sizeof(float));

	int i ;
	char archivo[100] = "carol.csv";	
	in = fopen(archivo, "r");	
	for(i=0;i<10;i++)
	{
		fscanf(in, "%f, %f, %f, %f, %f, %f, %f\n", &m[i], &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
		//printf("m= %f\n",m);
	}
	printf("PosicionX = %f\n",x[9]);
	printf("PosicionY = %f\n",y[9]);
	fclose(in);

	/*
	posx[0] = x
	posy[0] = y
	posz[0] = z
	velx[0] = vx
	vely[0] = v
	*/
	
	return 0;	
	
}




int inde(int i,int j)
{
	return 10*i+j;
}

float distancing (float xo,float xi,float y0,float y1,float z0, float z1)
{
 float distancia = sqrt(pow(x1-x0,2.0)+pow(y1-y0,2.0)+pow(z1-z0,2.0));
return distancia;
}

float acelex(float x0,float xi,float m,float r)
{
acelex = g*m*(x-x1)/pow(r,3.0)
}
/*float aceley(float x,float y,float m)
{
}
float acelez(float x,float y,float m)
{
}
*/



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



	
