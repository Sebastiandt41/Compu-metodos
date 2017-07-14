#miprimero.mk 

#all : Tarea1.pdf cargas.pdf err_integral.pdf num_integral.pdf

Tarea1.pdf : tarea.tex cargas.pdf err_integral.pdf num_integral.pdf	
	pdflatex $<

cargas.pdf : cargas.py 
	python cargas.py 

num_integral.pdf : integral.py 
	python integral.py 

err_integral.pdf : integral.py 
	python integral.py 

