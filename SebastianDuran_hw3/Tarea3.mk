
Resultados_hw3.pdf : Resultados_hw3.tex Onda2D_t30.png Onda2D_t60.png Onda3D_t30.png Onda3D_t60.png orbitas.png
	pdflatex $<
	rm datos.csv
	#rm *.png
	rm Resultados_hw3.log
	rm Resultados_hw3.aux
	rm Planetas.x

orbitas.png : Planetas.c Plots_Planetas.py
	cc Planetas.c -lm -o Planetas.x 
	./Planetas.x > datos.csv
	python Plots_Planetas.py

Onda2D_t30.png : Onda.py
	python Onda.py

Onda2D_t60.png : Onda.py
	python Onda.py

Onda3D_t30.png : Onda.py
	python Onda.py

Onda3D_t60.png : Onda.py
	python Onda.py

	


