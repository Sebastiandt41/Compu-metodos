#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define g 39.4793 //Unidades en UA y masas solares 

//pasar a masas solares las cosas del archivo

//como vamos a solucionar esta ecuacion diferencial loquete 

//10 AÑOS CON DT 0.001 SON 10000 POSICIONES , LUEGO SON 250 AÑOS CREO PARA LA VUELTA COMPLETA

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
	int tfinal = 10000
	float m[10];
	float *x = malloc((10*10000)*sizeof(float));
	float *y = malloc((10*10000)*sizeof(float));
	float *z = malloc((10*10000)*sizeof(float));
	float *vx = malloc((10*10000)*sizeof(float));
	float *vy = malloc((10*10000)*sizeof(float));
	float *vz = malloc((10*10000)*sizeof(float));
	float dt = 0.001
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

	for(t=1;t<tfinal;t++)
	{
		for(y=0;y<10;y++)
		{
		int indize = inde(t-1,y);
		float x0 = x[indize];
		float y0 = y[indize];
		float z0 = z[indize];
		//float m0 = m[y]
	//creo mis sumas pero aqui al final de este for necesito guardar las aceleraciones de todos mis planetas quietos para hacer leap frog 
		Ax = 0;
		Ay = 0;
		Az = 0;
	
			for(o=0;o<10;o++)
			{
					
			//COJO LO MIO Y LO COMPARO CON LOS DEMAS		
				if (o!=y){
					int indizo = inde(t-1,o);
				float x1 = x[indizo];
				float y1 = y[indizo];
				float z1 = z[indizo];
				float m1 = m[o];
				float dist = distancing(x0,x1,y0,y1,z0,z1);
					Ax+= acele(x0,x1,m1,dist);
					Ay+= acele(y0,y1,m1,dist);
					Az+= acele(z0,z1,m1,dist);
					}
			}
		Vx[indize] = Vx[indize] + 0.5*Ax*dt;
		Vy[indize] = Vy[indize] + 0.5*Ay*dt;
		Vz[indize] = Vz[indize] + 0.5*Az*dt;

		int index2 = inde(t,y);

		x[index2] = x[indize]+0.5*Vx[indize]*dt
		y[index2] = y[indize]+0.5*Vy[indize]*dt
		z[index2] = z[indize]+0.5*Vz[indize]*dt


		

		}
	}
	return 0;	
	
}




int inde(int t,int p)
{
	return 10*t+p;
}

float distancing (float xo,float xi,float y0,float y1,float z0, float z1)
{
 float distancia = sqrt(pow(x1-x0,2.0)+pow(y1-y0,2.0)+pow(z1-z0,2.0));
return distancia;
}

float acele(float yo,float el,float m,float r)
{
acelex = g*m*(el-yo)/pow(r,3.0);
return acele;
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



	
