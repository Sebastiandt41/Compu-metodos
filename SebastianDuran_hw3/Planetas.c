#include <stdlib.h>
#include <stdio.h>

#define g 39.4793 //Unidades en UA 


int main(void){
//primero con dos planetas, ver apuntes 
	FILE *in;
	float m, x, y, z, vx, vy, vz;
	int i ;
	char filename[100] = "coordinates.csv";	
	in = fopen(filename, "r");	
	for(i=0;i<10;i++){
	fscanf(in, "%f, %f, %f, %f, %f, %f, %f\n", &m, &x, &y, &z, &vx, &vy, &vz);
	printf("m= %f\n",m);
	}
	fclose(in);
	return 0;

	/*//distancias en AU 
	float masa;
	float posx[100];
	float posy[];
	float posz[100];
	float vx[100];
	float vy[100];
	float vz[100];
	
	int condiciones1[7];
	int condiciones2[7];
	
	float pos_solx = 0;
	float pos_soly = 0;	
	float pos_solz = 0;
	//en la realidad es del archivo 
	posx[0] = 13;
	posy[0] = 15;
	posz[0] = 25;
	vx[0] = 0;
	vy[0] = 0;
	vz[0] = 0;
	//Llamo la funcion que calcula la aceleracion 
	
	return 0;
	*/
}


	