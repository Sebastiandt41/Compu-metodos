#include <stdlib.h>
#include <stdio.h>
#define G 39.4783

float get_gravedad(float masa);

int main(void){
	//int t = 10;
	//print_algo(t);	
	FILE *in;
	//char CuerpoCeleste[100];
	//char *nombre;
	float masa, px, py, pz, velx, vely, velz;
	int i;
	char filename[100]="coordinates.csv";
	//char *split_CuerpoCeleste;
	//constant char delimiter;
	//delimiter =',';
	in = fopen(filename, "r");
	for(i=0;i<10;i++){
		//printf("value = %s\n",CuerpoCeleste);
		//split_CuerpoCeleste = strtok(CuerpoCeleste, delimiter); 
fscanf(in, "%f, %f, %f, %f, %f, %f, %f\n", &masa, &px, &py, &pz, &velx, &vely, &velz);

		//while(split_CuerpoCeleste != NULL)
		//{

		//}
		//masa, px, py, pz, velx, vely, velz = strtod(CuerpoCeleste, &nombre);
		
		printf("value = %f\n",masa);
	}
	fclose(in);
	return 0;
	}


/*void print_algo(t){
	int i;
	float masa;
	float poxMerc[t];
	float poyMerc[t];
	float pozMerc[t];
	float vxMerc[t];
	float vyMerc[t];
	float vzMerc[t];	

	//Suponemos que el sol no se mueve
	float PosicionSolx = 0.0;
	float PosicionSoly = 0.0;
	float PosicionSolz = 0.0;
	
	float poxMerc[0]=0.3615;
	float poyMerc[0]=-0.027;
	float pozMerc[0]=-0.0355;
	
	float vxMerc[0]=-1.11846;
	float vyMerc[0]=10.7016;
	float vxMerc[0]=0.9768;

	for (i=1; i<t;i++){
		poxMerc[i] 
	}
	return 0;
	

}*/

	
