
PuntoNemo.pdf : Plots.py datos.csv
	python Plots.py
	rm datos.csv
	rm a.out

a.out : GeographicPoint.c 
	cc GeographicPoint.c	

datos.csv : a.out
	cc GeographicPoint.c -lm
	./a.out	
	

	



	
	
