#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int lista[10];
	int i;
	printf("Contenido antes de inicializar\n");
	for(i=0;i<10;i++)
	{
	printf("%d\n",lista[i]);
	}

	int n_points;
	int *array_int;
	n_points =10;
	array_int = malloc(n_points*sizeof(2));
	if(!array_int)
	{
	printf("There is something wrong with arrat int\n");
	exit(1);
	}
	printf("Memory starts at %p\n",array_int);
	printf("Allocation went OK.Initializing...\n");
	for(i=0;i<n_points;i++)
	{
	array_int[i] = i*2;
	printf("%d\n",array_int[i]);
	}
	printf("Lets see what happens if I go a bit beyond the allocated space...\n");

	array_int[n_points] = n_points*2;
	printf("%d\n",array_int[n_points]);
	printf("OK");
	printf("and if i go far away?\n");
	array_int[n_points*1000] = n_points*1000*2;
	printf("%d\n",array_int[n_points*1000]);
	printf("everything went just fine\n");
	return 0;




}

