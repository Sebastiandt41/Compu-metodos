#include <stdlib.h>
#include <stdio.h>

#define g 39.4793 //Unidades en UA 


int main(void)
{
//primero con dos planetas, ver apuntes 
	FILE *in;
	float m,x,y,z,vx,vy,vz;
	int i ;
	char filename[100] = "coordinates.csv";	
	in = fopen(filename, "r");	
	for(i=0;i<10;i++)
	{
		fscanf(in, "%f, %f, %f, %f, %f, %f, %f\n", &m, &x, &y, &z, &vx, &vy, &vz);
		printf("m= %f\n",m);
	}
	fclose(in);
	return 0;
	
}
	






	
	


