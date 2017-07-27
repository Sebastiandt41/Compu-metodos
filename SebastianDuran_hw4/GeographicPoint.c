#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <time.h>

int indice(int x , int y);
float radius(int posx,int posy, int *posicion);
int aleatorio_x();
int aleatorio_y();
int i,j;
int largo = 744;
int alto = 500;

int main(void)
{
	int a,b,k;
	//Cargo los datos 
	int *posicion = malloc((largo*alto)*sizeof(int));
	FILE *in;
	char mapa[100] = "map_data.txt";
	in = fopen(mapa,"r");
	for(b=0;b<alto;b++)
	{
		for(a=0;a<largo;a++)
		{
		fscanf(in,"%d\n",&posicion[indice(a,b)]);
		//printf("posicion %d\n",posicion[indice(i,j)]);
		}
	}
	fclose(in);
	

	srand(1);
	

	//MARKOV CHAIN 
	
	int n_pasos = 5000;
	float beta;
	int xa = aleatorio_x();
	int ya = aleatorio_y();
	float r_inicial = radius(xa,ya,posicion);
	float r_new;
	int x_max ;
	int y_max ;
	float r_maximo = 0;
	int x_new, y_new;
	float alpha;

	for(k=0; k < n_pasos;k++)
	{	
		//printf("%d\n",k);
		x_new = xa+aleatorio_x();
		if(x_new<0)
		{x_new = largo + x_new%largo;}
		else if(x_new >largo)
		{x_new =x_new%largo;}
		y_new = ya+aleatorio_y();
		if(y_new<0)
		{y_new = alto + y_new%alto;}
		else if(y_new>alto)
		{y_new=y_new%largo;}	
		
	r_new = radius(x_new,y_new,posicion);
	
	alpha = r_new/r_inicial ;
	
		if(alpha > 1.0)
		{
		xa = x_new;
		ya = y_new;
		r_inicial = r_new;
		}
		else if(alpha <1.0)
		{
		//beta = rand()/RAND_MAX;
		beta = drand48();
			if(beta < alpha)
			{
			xa = x_new;
			ya = y_new;
			r_inicial = r_new;
			}
			else if(beta > alpha)
			{
			continue;
			//xa = xa;
			//ya = ya;
			//r_inicial = radius(xa,ya,posicion);
			}
		}
	if(r_new>r_maximo)
	{
	r_maximo = r_new;
	x_max = x_new;
	y_max = y_new;	
	}
	
	}
	printf("%f %d %d\n",r_maximo,x_max,y_max);
	
return 0;
}

int indice(int x, int y)
{
	if(x<0)
	{x= largo + x%largo;}
	else if(x>largo)
	{x=x%largo;}
	if(y<0)
	{y = alto + y%alto;}
	else if(y>alto)
	{y=y%largo;}

int ind = alto*x+y;

return ind;
}

int aleatorio_x()
{
	int x_alea = rand()% (largo/4+1) - largo/8 ;
	//int x_alea = rand()%largo/5;
	return x_alea;
}
int aleatorio_y()
{
	int y_alea = rand()% (alto/2+1) - largo/4;
	//int y_alea = rand()%alto/3;
	return y_alea;
}
float radius(int posix,int posiy, int *posicion)
{
	//int i,j ;	
	float comp;
	float r_max;
	float r ;
	for(r = 1; r < alto/2 ; r++)
	{
		for(i=0;i<r;i++)
		{
			for(j = 0; j< r;j++)
			{
			//printf("%d %d\n",i,j);
			//printf("%d\n",posicion[indice(i,j)]);
				if(((i*i)+(j*j))<r*r)
				{
					if(posicion[indice(posix+i,posiy)]==0 && posicion[indice(posix,posiy+j)]==0 && posicion[indice(posix-i,posiy)]==0 && posicion[indice(posix,posiy-j)]==0 && posicion[indice(posix+i,posiy+j)]==0 && posicion[indice(posix-i,posiy-j)]==0 && posicion[indice(posix+i,posiy-j)]==0 && posicion[indice(posix-i,posiy+j)]==0)
					{					
					r_max = r;			
					}
					else
					{
					r_max = r-1;
					comp = r_max;
					break;
					}
				}
			if(comp == r_max){break;}
			}		
		if(comp == r_max){break;}
		}
	if(comp == r_max){break;}
	}
	return r_max;	

}















