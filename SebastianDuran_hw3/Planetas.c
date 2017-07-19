#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>

#define g 39.4793 //Unidades en UA y masas solares 

//DECLARACION DE FUNCIONES

int indice(int p,int t);
float distancing (float xo,float xi,float y0,float y1,float z0, float z1);
void calculo(float *m,float *x,float *y,float *z,float *Vx,float *Vy, float *Vz);
float acele(float yo,float el,float m,float r);
float cambio_masa(float m);
float acelerando(float ax , float ay, float az);
//EL MAIN 
int main(void)
{
	FILE *in;
	float dt = 2.74E-3;
	
	int tfinal = 365*255;
	float *mkg = malloc(10*sizeof(float));
	float *m = malloc(10*sizeof(float));
	float *x = malloc((10*tfinal)*sizeof(float));
	float *y = malloc((10*tfinal)*sizeof(float));
	float *z = malloc((10*tfinal)*sizeof(float));
	float *vxi = malloc(10*sizeof(float));
	float *vyi = malloc(10*sizeof(float));
	float *vzi = malloc(10*sizeof(float));
	float *vx = malloc((10*tfinal)*sizeof(float));
	float *vy = malloc((10*tfinal)*sizeof(float));
	float *vz = malloc((10*tfinal)*sizeof(float));
	float *ax = malloc(10*sizeof(float));
	float *ay = malloc(10*sizeof(float));
	float *az = malloc(10*sizeof(float));
	
	int i,k,pi;
	int ii;
	int t;
	//LEO EL ARCHIVO
	char archivo[100] = "coordinates.csv";	
	
	in = fopen(archivo, "r");
	int len =250;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter =",";
	int j=0;
	i = 0;
	while(fgets(line_buffer,len,in))
	{
	split_buffer = strtok(line_buffer,delimiter);
	while(split_buffer != NULL)
	{
	if(j==1)
		mkg[i] = atof(split_buffer);
	else if(j==2)
		x[i] = atof(split_buffer);
	else if(j==3)
		y[i] = atof(split_buffer);
	else if(j==4)
		z[i] = atof(split_buffer);
	else if(j==5)
		vx[i] = atof(split_buffer);
	else if(j==6)
		vy[i] = atof(split_buffer);
	else if(j==7)
		vz[i] = atof(split_buffer);
	split_buffer = strtok(NULL,delimiter);
	j++;
	}
	j=0;
	i++;
	}
	fclose(in);
	//Convierto las masas de kg a masas solares
	for(i=0;i<10;i++)
	{
	m[i]=cambio_masa(mkg[i]);
	//printf("m2= %f\n",m[i]); PRUEBA QUE LA MASA FUNCIONA
	}
	//void aceleracion(float x //Primeras aceleraciones t = 0
	for(i=0;i<10;i++)
	{
	ax[i]=0;
	ay[i]=0;
	az[i]=0;
		for(ii=0;ii<10;ii++)
		{
			if(i!=ii)
			{
			float dist = distancing(x[i],x[ii],y[i],y[ii],z[i],z[ii]);
			ax[i]+=	acele(x[i],x[ii],m[ii],dist);
			ay[i]+= acele(y[i],y[ii],m[ii],dist);
			az[i]+= acele(z[i],z[ii],m[ii],dist);
			}			
	// //PRUEBA QUE LA ACELERACION FUNCIONA
		}
	//printf("Aceleracion en i = %f\n",ax[i]);
	}
	//modifico las velocidades para desfasarlas 
	//for(i=0;i<10;i++)
	//{
	//vx[i]= vx[i]-0.5*ax[i]*dt;
	//vy[i]= vy[i]-0.5*ax[i]*dt;
	//vz[i]= vz[i]-0.5*ax[i]*dt;	
	//}
	
	//Calculo los siguientes pasos de mis aceleraciones, velocidades, posiciones
	for(t=1;t<tfinal;t++)
	{		
		for(i=0;i<10;i++)
		{
		int ind_fut = indice(i,t);
		int ind_past = indice(i,t-1);

		vxi[i]=vx[ind_past]+0.5*ax[i]*dt;
		vyi[i]=vy[ind_past]+0.5*ay[i]*dt;
		vzi[i]=vz[ind_past]+0.5*az[i]*dt;
		
		x[ind_fut]= x[ind_past]+vxi[i]*dt;
		y[ind_fut]= y[ind_past]+vyi[i]*dt;
		z[ind_fut]= z[ind_past]+vzi[i]*dt;
												
		}
		for(i=0;i<10;i++)
		{
		int ind_mio = indice(i,t);
		int ind_past = indice(i,t-1);		
		ax[i] = 0;
		ay[i] = 0;
		az[i] = 0;
			for(ii=0;ii<10;ii++)
			{
				int ind_otro = indice(ii,t);
				if(i!=ii)
				{
				float dist = distancing(x[ind_mio],x[ind_otro],y[ind_mio],y[ind_otro],z[ind_mio],z[ind_otro]);
				ax[i]+=	acele(x[ind_mio],x[ind_otro],m[ii],dist);
				ay[i]+= acele(y[ind_mio],y[ind_otro],m[ii],dist);
				az[i]+= acele(z[ind_mio],z[ind_otro],m[ii],dist);
				}
			}
	
		vx[ind_mio] =vxi[i]+0.5*ax[i]*dt;
		vy[ind_mio] =vyi[i]+0.5*ay[i]*dt;
		vz[ind_mio] =vzi[i]+0.5*az[i]*dt;
		}

			
	}


for(i=0;i<tfinal*10;i++)
{
	printf("%f,%f,%f\n",x[i],y[i],z[i]);	
}

	return 0;

	
}

//DECLARO LAS DEMAS FUNCIONES 

/*int indice(int p,int t) SI LE PIDO UN DATO A MI MEGA ARRAY
{
	int t_total = 10000;
	int posicion = t_total*t + p;
	return posicion;
}
*/

//Si guardo un dato en el mega array 
int indice(int p,int t) //SI guardo UN DATO A MI MEGA ARRAY
{
	int posicion = 10*t + p;
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
	float aceler = g*m*(el-yo)/(r*r*r);
return aceler;
}
/*
void acelerando(float ax , float ay, float az , float x0, float x1, float y0, float y1, float z1, float z1)
{
	float ax = 0;
	float ay = 0;
	float az = 0;
	int i,ii;
	for(i=0;i<10;i++)
	{
		for(ii=0;ii<10;ii++)
		{
		if(i!=ii){
		float dist = distancing(x[i],x[ii],y[i],y[ii],z[i],z[ii]);
		ax[i]+=	acele(x[i],x[ii],m[ii],dist);
		ay[i]+= acele(y[i],y[ii],m[ii],dist);
		az[i]+= acele(z[i],z[ii],m[ii],dist);
		}			
	//printf("Aceleracion en i = %f\n",ax[i]); //PRUEBA QUE LA ACELERACION FUNCIONA
	}

}

*/











