#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <time.h>


float func(float x);
float aleat_x();
float integral(float suma,float dt);


int main(void)
{
	int i;
	srand48(time(NULL));
	int a = 0;
	int b = 1;	
	int puntos = 100000;
	float dt = ((b-a)/(puntos-1.0));
	float suma = 0;	

	for(i=0;i<puntos;i++)
	{
		float valor = func(aleat_x());
		suma += valor;	
	}

	float resultado = integral(suma,dt);

	FILE *on;
	char filen[100] = "resultados.txt";
	on = fopen(filen,"w");
	fprintf(on,"El valor de la integral es :%f\n",resultado);
	fclose(on);
	
return 0;
}

float func(float x)
{
	float y = exp(-(x));
	return y;

}
float aleat_x()
{
	int max = 1;
	int min = 0;
	float x = ((max-min)*drand48() + min);
	return x;
}

float integral(float suma,float dt)
{
	float integrali = suma*dt;
	return integrali;

}











