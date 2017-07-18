#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define g 39.4793 //Unidades en UA y masas solares 

/*pasar a masas solares las cosas del archivo

como vamos a solucionar esta ecuacion diferencial loquete 
10 AÑOS CON DT 0.001 SON 10000 POSICIONES , LUEGO SON 250 AÑOS CREO PARA LA VUELTA COMPLETA
*/




//DECLARACION DE FUNCIONES

int inde(int t,int p);
float distancing (float xo,float xi,float y0,float y1,float z0, float z1);
void calculo(float *m,float *x,float *y,float *z,float *Vx,float *Vy, float *Vz);
float acele(float yo,float el,float m,float r);
//EL MAIN 
int main(void)
{
	FILE *in;

	
	

	float *m = malloc(10*sizeof(float));
	float *x = malloc((10*10000)*sizeof(float));
	float *y = malloc((10*10000)*sizeof(float));
	float *z = malloc((10*10000)*sizeof(float));
	float *vx = malloc((10*10000)*sizeof(float));
	float *vy = malloc((10*10000)*sizeof(float));
	float *vz = malloc((10*10000)*sizeof(float));
	
	int i ;
	//LEO EL ARCHIVO
	char archivo[100] = "carol.csv";	
	in = fopen(archivo, "r");	
	for(i=0;i<10;i++)
	{
		fscanf(in, "%f, %f, %f, %f, %f, %f, %f\n", &m[i], &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
		//printf("m= %f\n",m);
	}
	fclose(in);



	return 0;	
	
}


//DECLARO LAS DEMAS FUNCIONES 

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
return acelex;
}

void calculo(float *m,float *x,float *y,float *z,float *Vx,float *Vy, float *Vz)
{
	float dt = 0.001
	int tfinal = 10000;
	int t,p,o;
	int ind1 ;
	int ind2 ;
	float x0,y0,z0,x1,y1,z1,m1,dist

	for(t=1;t<tfinal;t++)
	{
		for(p=0;p<10;p++)
		{
		ind1 = inde(t-1,p);
		 x0 = x[ind1];
		 y0 = y[ind1];
		 z0 = z[ind1];
		
	//creo mis sumas pero aqui al final de este for necesito guardar las aceleraciones de todos mis planetas quietos para hacer leap frog 
		Ax = 0;
		Ay = 0;
		Az = 0;	
			for(o=0;o<10;o++)
			{					
					
				if (o!=p){
				ind2 = inde(t-1,o);
				 x1 = x[ind2];
				 y1 = y[ind2];
				 z1 = z[ind2];
				 m1 = m[o];
				 dist = distancing(x0,x1,y0,y1,z0,z1);
					Ax+= acele(x0,x1,m1,dist);
					Ay+= acele(y0,y1,m1,dist);
					Az+= acele(z0,z1,m1,dist);
					}
			}
		
		int index2 = inde(t,p);
	
		if(k==1){
		Vx[ind1] = Vx[ind1] + 0.5*Ax*dt;
		Vy[ind1] = Vy[ind1] + 0.5*Ay*dt;
		Vz[ind1] = Vz[ind1] + 0.5*Az*dt;

		x[index2] = x0+0.5*Vx[ind1]*dt;
		y[index2] = y0+0.5*Vy[ind1]*dt;
		z[index2] = z0+0.5*Vz[ind1]*dt;
			}
		else
		{
		Vx[index2] = Vx[ind1] + 0.5*Ax*dt;
		Vy[index2] = Vy[ind1] + 0.5*Ay*dt;
		Vz[index2] = Vz[ind1] + 0.5*Az*dt;

		x[index2] = x0+Vx[ind1]*dt
		y[index2] = y0+Vy[ind1]*dt
		z[index2] = z0+Vz[ind1]*dt
		}

		}
	}

}









	
