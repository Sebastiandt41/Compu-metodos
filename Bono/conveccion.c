#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void cond_inicial(double *u, int n_x , double d_x);
void primer_u(double *u_actual,double *u_inicial, double n_x , double r);
void actualizar_u(double *u_fut,double *u_actual,double n_x, double r );
void copiar(double *u_nuevo,double *u_viejo,double n_x);
void print_u(double *u,double n_x,double d_x);

int main()
{
	double x_f = 2.0 ;
	int n_x = 100 ;
	double d_x = (x_f)/(n_x-1.0);
	double t_f = 0.3;
	int n_t = 300;
	double d_t = (t_f)/(n_t - 1);
	double c = 1.0;
	double r = c*(d_t/d_x);
	
	double *u_viejo = malloc(n_x*sizeof(double));
	double *u_actual = malloc(n_x*sizeof(double));
	double *u_fut = malloc(n_x*sizeof(double));

	cond_inicial(u_viejo,n_x,d_x);
	u_viejo[0] = 0;
	u_viejo[n_x-1] =0;
	
	primer_u(u_actual,u_viejo,n_x,r);
	int i;
	for (i=0;i<n_t;i++)
	{
	actualizar_u(u_fut,u_actual,n_x,r);
	copiar(u_actual,u_viejo,n_x);
	copiar(u_fut,u_actual,n_x);
	}
	
	print_u(u_actual,n_x,d_x);
	return 0;	
}
	
void cond_inicial(double *u, int n_x, double d_x)
{
	int i;
	for(i=0;i<n_x;i++)
	{
	double x = i*d_x;
		if(x >= 0.7 && x<= 1.2)
		{
		u[i] = 2;
		}		
		else 
		{
		u[i] = 0;
		}
	}
}
void primer_u(double *u_actual, double *u_inicial, double n_x, double r)
{
int i;
	for(i=1;i<n_x-1;i++)
	{
	u_actual[i] = u_inicial[i] - r*(u_inicial[i]-u_inicial[i-1]);
	}
}
void actualizar_u(double *u_fut, double *u_actual, double n_x, double r)
{
int i;
	for(i=1;i<n_x-1;i++)
	{
	u_fut[i] = u_actual[i] - r*(u_actual[i]-u_actual[i-1]);
	}
}
void copiar(double *u_nuevo,double *u_viejo, double n_x)
{
int i ;
	for(i=0;i<n_x;i++)
	{
	u_viejo[i] = u_nuevo[i];
	}
}
void print_u(double *u, double n_x,double d_x)
{
int i;
	for(i=0;i<n_x;i++)
	{
	printf("%f %f\n",i*d_x,u[i]);
	}
}











































