#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define g 39.4793 //Unidades en UA y masas solares 

/*pasar a masas solares las cosas del archivo

como vamos a solucionar esta ecuacion diferencial loquete 
10 AÑOS CON DT 0.001 SON 10000 POSICIONES , LUEGO SON 250 AÑOS CREO PARA LA VUELTA COMPLETA
*/




//DECLARACION DE FUNCIONES

int indice(int p,int t);
float distancing (float xo,float xi,float y0,float y1,float z0, float z1);
void calculo(float *m,float *x,float *y,float *z,float *Vx,float *Vy, float *Vz);
float acele(float yo,float el,float m,float r);
float cambio_masa(float m);
//EL MAIN 
int main(void)
{
	FILE *in;

	int tfinal = 10000;
	float *mkg = malloc(10*sizeof(float));
	float *m = malloc(10*sizeof(float));
	float *x = malloc((10*tfinal)*sizeof(float));
	float *y = malloc((10*10000)*sizeof(float));
	float *z = malloc((10*10000)*sizeof(float));
	float *vx = malloc((10*10000)*sizeof(float));
	float *vy = malloc((10*10000)*sizeof(float));
	float *vz = malloc((10*10000)*sizeof(float));
	float *ax = malloc((10)*sizeof(float));
	float *ay = malloc((10)*sizeof(float));
	float *az = malloc((10)*sizeof(float));
	
	int i ;
	int ii;
	int t;
	//LEO EL ARCHIVO
	char archivo[100] = "carol.csv";	
	in = fopen(archivo, "r");	
	for(i=0;i<10;i++)
	{
		fscanf(in, "%f, %f, %f, %f, %f, %f, %f\n", &mkg[i], &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
	}
	fclose(in);
	//Convierto las masas de kg a masas solares
	for(i=0;i<10;i++)
	{
	m[i]=cambio_masa(mkg[i]);
	//printf("m2= %f\n",m[i]); PRUEBA QUE LA MASA FUNCIONA
	}
	//Primeras aceleraciones t = 0
	for(i=0;i<10;i++){
	ax[i]=0;
	ay[i]=0;
	az[i]=0;
		for(ii=0;ii<10;ii++)
		{
		if(i!=ii){
		float dist = distancing(x[i],x[ii],y[i],y[ii],z[i],z[ii]);
		ax[i]+=	acele(x[i],x[ii],m[ii],dist);
		ay[i]+= acele(y[i],y[ii],m[ii],dist);
		az[i]+= acele(z[i],z[ii],m[ii],dist);
		}			
		}
	//printf("Aceleracion en i = %f\n",ax[i]); PRUEBA QUE LA ACELERACION FUNCIONA
	}
	//Calculo los siguientes pasos de mis aceleraciones, velocidades, posiciones
	for(t=1;t<tfinal;


	calculo(m,x,y,z,vx,vy,vz);
	for(i=0;i<1000;i++)
	{
	printf("x = %f\n",x[i]);
	}

	return 0;	
	
}


//DECLARO LAS DEMAS FUNCIONES 

int indice(int p,int t)
{
	int t_total = 10000;
	int posicion = t_total*t + p;
	return posicion;
}
float cambio_masa(float m)
{
	float m1 = m*(1.0/1.9891E30);
	return m1;
}
float distancing (float x0,float x1,float y0,float y1,float z0, float z1)
{
	float distancia = sqrt((pow(x1-x0,2.0)+pow(y1-y0,2.0)+pow(z1-z0,2.0))+0.01);
	return distancia;
}

float acele(float yo,float el,float m,float r)
{
	float aceler = g*m*(el-yo)/pow(r,3.0);
return aceler;
}

void calculo(float *m,float *x,float *y,float *z,float *Vx,float *Vy, float *Vz)
{
	float dt = 0.001;
	int tfinal = 10000;
	int t,p,o;
	int ind1 ;
	int ind2 ;
	float x0,y0,z0,x1,y1,z1,m1,dist,Ax,Ay,Az;

	for(t=1;t<tfinal;t++)
	{
		
		for(p=0;p<10;p++)
		{
		ind1 = indice(p,t-1);
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
				ind2 = indice(o,t-1);
				 x1 = x[ind2];
				 y1 = y[ind2];
				 z1 = z[ind2];
				 m1 = m[o];
				 dist = distancing(x0,x1,y0,y1,z0,z1);
				
					Ax+= acele(x0,x1,m1,dist);
					Ay+= acele(y0,y1,m1,dist);
					Az+= acele(z0,z1,m1,dist);
				//printf("x=%f\n",x1);
					}
			}
		
		int index2 = indice(p,t);
	
		if(t==1){
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

		x[index2] = x0+Vx[ind1]*dt;
		y[index2] = y0+Vy[ind1]*dt;
		z[index2] = z0+Vz[ind1]*dt;
		}

		}
	}

}










	
