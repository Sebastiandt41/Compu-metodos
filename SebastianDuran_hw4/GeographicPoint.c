#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <time.h>

int indice(int x , int y);
float radius(int posx,int posy, int *posicion);
int aleatorio_x();
int aleatorio_y();

int largo = 744;
int alto = 500;
int i ;
int j ;

int main(void)
{
	//Cargo los datos 
	int *posicion = malloc((largo*alto)*sizeof(int));
	FILE *in;
	char mapa[20] = "map_data.txt";
	in = fopen(mapa,"r");
	for(j=0;j<alto;j++)
	{
		for(i=0;i<largo;i++)
		{
		fscanf(in,"%d\n",&posicion[indice(i,j)]);
		//printf("posicion %d\n",posicion[indice(i,j)]);
		}
	}
	fclose(in);
	

	srand(time(NULL));
	
	
	//printf("ra = %f\n",ra);
	
	//printf("aleatorios = %d %d\n",x_a,y_a);

	//printf("posicion = %d\n",posicion[indice(217,236)]); //=0
	//printf("posicion = %d\n",posicion[indice(230,234)]); //=1

	//MARKOV CHAIN 
	int n_pasos = 100;
	int xa = aleatorio_x();
	int ya = aleatorio_y();
	float r_inicial = radius(xa,ya,posicion);
	float r_new;
	int x_new, y_new;
	float alpha;

	for(i=0; i < n_pasos;i++)
	{
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
	
		if(alpha > 1)
		{
		xa = x_new;
		ya = y_new;
		r_inicial = r_new;
		}
		else if(alpha <1)
		{
		float beta = rand()/RAND_MAX;
			if(beta < alpha)
			{
			xa = x_new;
			ya = y_new;
			r_inicial = r_new;
			}
			else if(beta > alpha)
			{
			continue;
			}
		}

	}
	printf("El radio,posx,posy es = %f %d %d\n",r_inicial,xa,ya);

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
	int x_alea = rand()% (largo/5+1) - largo/10 ;
	//int x_alea = rand()%largo/5;
	return x_alea;
}
int aleatorio_y()
{
	int y_alea = rand()% (alto/3+1) - largo/6;
	//int y_alea = rand()%alto/3;
	return y_alea;
}
float radius(int posix,int posiy, int *posicion)
{
	float comp;
	float r_max;
	float r ;
	for(r = 1; r < alto/2 ; r++)
	{
		for(i=0;i<r;i++)
		{
			for(j = 0; j< r;j++)
			{
				if(((i*i)+(j*j))<r*r)
				{
					if(posicion[indice(posix+i,posiy)]==0 && posicion[indice(posix,posiy+j)]==0 && posicion[indice(posix-i,posiy)]==0 && posicion[indice(posix,posiy-j)]==0 && posicion[indice(posix+i,posiy+j)]==0 && posicion[indice(posix-i,posiy-j)]==0 && posicion[indice(posix+i,posiy-j)]==0 && posicion[indice(posix-i,posiy+j)]==0)
					{
					
					r_max = r;
										
					}
					else
					{
					r_max = r;
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















