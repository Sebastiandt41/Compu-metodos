#include <stdlib.h>
#include <math.h>
#include <stdio.h>

void cargar_datos(char Archiv);
int indice(int x , int y);
float get_radio(int x0, int x1, int y0, int y1);
int sampleo_mc();

	
	int largo = 744;
	int alto = 500;
	int i ;
	int j ;

int main(void)
{
	int *posicion = malloc((largo*alto)*sizeof(int));

	FILE *in;
	char mapa[20] = "map_data.txt";
	in = fopen(mapa,"r");
	for(j=0;j<alto;j++)
	{
		for(i=0;i<largo;i++)
		{
			fscanf(in,"%d\n",&posicion[indice(i,j)]);	
		}
	}
	printf("posicion = %d\n",posicion[indice(217,236)]); //=0
	printf("posicion = %d\n",posicion[indice(230,234)]); //=1


return 0;
}



int indice(int x, int y)
{
	int ind = alto*x+y;
	return ind;
}

float get_radio(int x0,int x1,int y0,int y1)
{
	float r = sqrt(((x1-x0)*(x1-x0))+((y1-y0)*(y1-y0)));
	return r;
}









