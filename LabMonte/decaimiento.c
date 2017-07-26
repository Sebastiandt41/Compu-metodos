#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float gam = 0.5;
float n_0 = 10.0;
int t_f = 10;
double d_t = 0.01;
int n_iteraciones = 200;

void condicion_i(double *u, int t_f,double d_t);

void decaimiento_1(float n, float *n_inicial);
void decaimiento_2(float n, float *n_temporal);
float delta_n_step(float n);

int main(void)
{
	int i,j;
	double *u_actual = malloc(1000*sizeof(double));
	float *n_inicial = malloc(1000*sizeof(float));
	float *n_temporal = malloc(1000*sizeof(float));

	
	condicion_i(u_actual,t_f,d_t);
	
	
	
	srand(1);	
	
	decaimiento_1(n_0,n_inicial);
	
	for(i=0;i<n_iteraciones;i++)
	{
		for(j=0;j<1000;j++)
		{
		decaimiento_2(n_0,n_temporal);
		n_inicial[j] += n_temporal[j];
		}	
	}	
	for(i=0;i<n_iteraciones;i++)
	{
	n_inicial[i] = n_inicial[i]/n_iteraciones;	
	}	
	
	for(i=0;i<1000;i++)
		{
		printf("%f %f %f\n",u_actual[i],n_inicial[i],i*d_t);
		
		}



return 0;
}

void condicion_i(double *u,int t_f,double d_t)
{	
	int i;
	for(i=0;i<1000;i++)
	{
		
		u[i] = n_0*exp(-0.5*(i*d_t));
	}

	
}

//drand48() funcion que me genera un numero aleatorio entre 0 y 1 


void decaimiento_1(float n , float *n_inicial)
{	
	int i ;
	float t = 0.0;
	float N = n;
	
	for(i=0;i<1000;i++)
	{
	t+= d_t;
	float d_n = delta_n_step(N);
	
	N+= d_n;
	
	n_inicial[i] = N;
	
	//printf("%f %f\n",N,t);
	
	}
}

void decaimiento_2(float n,float *n_temporal)
{	
	int i ;
	float t = 0.0;
	float N = n;
	
	for(i=0;i<1000;i++)
	{
	t+= d_t;
	float d_n = delta_n_step(N);
	
	N+= d_n;
	
	n_temporal[i] = N;
	
	//printf("%f %f\n",N,t);
	
	}
}

float delta_n_step(float n)
{
float num_ale = drand48();
float Po = gam*n*d_t;

	if(num_ale<Po)
	{
	return -1;
	}
	else
	{
	return 0;
	}
}


















